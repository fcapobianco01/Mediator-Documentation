## Group 1

### This group contains a very weird design of data structure and memory allocation. Easy to get wrong, hard to verify even by manual inspection.

- https://github.com/torvalds/linux/blob/v3.19/security/selinux/xfrm.c#L98
```c
static int selinux_xfrm_alloc_user(struct xfrm_sec_ctx **ctxp,
				   struct xfrm_user_sec_ctx *uctx,
				   gfp_t gfp)
{
	int rc;
	const struct task_security_struct *tsec = current_security();
	struct xfrm_sec_ctx *ctx = NULL;
	u32 str_len;

	if (ctxp == NULL || uctx == NULL ||
	    uctx->ctx_doi != XFRM_SC_DOI_LSM ||
	    uctx->ctx_alg != XFRM_SC_ALG_SELINUX)
		return -EINVAL;

	str_len = uctx->ctx_len;
	if (str_len >= PAGE_SIZE)
		return -ENOMEM;

	ctx = kmalloc(sizeof(*ctx) + str_len + 1, gfp);               <<== This line
	if (!ctx)
		return -ENOMEM;

	ctx->ctx_doi = XFRM_SC_DOI_LSM;
	ctx->ctx_alg = XFRM_SC_ALG_SELINUX;
	ctx->ctx_len = str_len;
	memcpy(ctx->ctx_str, &uctx[1], str_len);					 <<== Suspicious
	ctx->ctx_str[str_len] = '\0';
...
}
```

- https://github.com/torvalds/linux/blob/v3.19/security/selinux/xfrm.c#L289
```c
int selinux_xfrm_policy_alloc(struct xfrm_sec_ctx **ctxp,
			      struct xfrm_user_sec_ctx *uctx,
			      gfp_t gfp)
{
	return selinux_xfrm_alloc_user(ctxp, uctx, gfp);              <<== This line
}
```

The `memcpy` function call in the `selinux_xfrm_alloc_user` function is copying 
`str_len` bytes from **`&uctx[1]`** to the `ctx->ctx_str` buffer. 
The `str_len` variable is derived from the `uctx->ctx_len` field, where `uctx` 
is a kernel-controlled input.

The `xfrm_user_sec_ctx` structure is defined as follows:
```c
struct xfrm_user_sec_ctx {
	__u16			len;
	__u16			exttype;
	__u8			ctx_alg;  /* LSMs: e.g., selinux == 1 */
	__u8			ctx_doi;
	__u16			ctx_len;
};
```
But the stringified context string is actually stored *after the corresponding structure*?

## Group 2
### This group contains a safely bounded variable index, which we can safely discard.

- https://github.com/torvalds/linux/blob/v3.19/security/selinux/avc.c#L678
```c
static noinline struct avc_node *avc_compute_av(u32 ssid, u32 tsid,
			 u16 tclass, struct av_decision *avd)
{
	rcu_read_unlock();
	security_compute_av(ssid, tsid, tclass, avd);
	rcu_read_lock();
	return avc_insert(ssid, tsid, tclass, avd);                   <<== This line 
}
```

- https://github.com/torvalds/linux/blob/v3.19/security/selinux/avc.c#L398
- https://github.com/torvalds/linux/blob/v3.19/security/selinux/avc.c#L399
```c
static struct avc_node *avc_insert(u32 ssid, u32 tsid, u16 tclass, struct av_decision *avd)
{
	struct avc_node *pos, *node = NULL;
	int hvalue;
	unsigned long flag;

	if (avc_latest_notif_update(avd->seqno, 1))
		goto out;

	node = avc_alloc_node();
	if (node) {
		struct hlist_head *head;
		spinlock_t *lock;

		hvalue = avc_hash(ssid, tsid, tclass);                    <<== Assignment here
		avc_node_populate(node, ssid, tsid, tclass, avd);

		head = &avc_cache.slots[hvalue];                          <<== This line 
		lock = &avc_cache.slots_lock[hvalue];                     <<== This line 

		spin_lock_irqsave(lock, flag);
		hlist_for_each_entry(pos, head, list) {
			if (pos->ae.ssid == ssid &&
			    pos->ae.tsid == tsid &&
			    pos->ae.tclass == tclass) {
				avc_node_replace(node, pos);
				goto found;
			}
		}
		hlist_add_head_rcu(&node->list, head);
found:
		spin_unlock_irqrestore(lock, flag);
	}
out:
	return node;
}
```

The variable index `hvalue` is bounded by the  assignment in the `avc_hash` function.
With the fields `slots` and `slots_lock` being arrays of size `AVC_CACHE_SLOTS` (512).
Related code:
```c
#define AVC_CACHE_SLOTS			512

struct avc_cache {
	struct hlist_head	slots[AVC_CACHE_SLOTS]; /* head for avc_node->list */
	spinlock_t		    slots_lock[AVC_CACHE_SLOTS]; /* lock for writes */
	atomic_t		    lru_hint;	/* LRU hint for reclaim scan */
	atomic_t		    active_nodes;
	u32			        latest_notif;	/* latest revocation notification */
};

static inline int avc_hash(u32 ssid, u32 tsid, u16 tclass)
{
	return (ssid ^ (tsid<<2) ^ (tclass<<4)) & (AVC_CACHE_SLOTS - 1);
}
```

## Group 3
### This group contains a safely bounded variable index, which we can safely discard. Same as Group 2.

- https://github.com/torvalds/linux/blob/v3.19/security/selinux/avc.c#L282
```c
static struct avc_node *avc_alloc_node(void)
{
	struct avc_node *node;

	node = kmem_cache_zalloc(avc_node_cachep, GFP_ATOMIC|__GFP_NOMEMALLOC);
	if (!node)
		goto out;

	INIT_HLIST_NODE(&node->list);
	avc_cache_stats_incr(allocations);

	if (atomic_inc_return(&avc_cache.active_nodes) > avc_cache_threshold)
		avc_reclaim_node();										  <<== This line

out:
	return node;
}

```
- https://github.com/torvalds/linux/blob/v3.19/security/selinux/avc.c#L246
- https://github.com/torvalds/linux/blob/v3.19/security/selinux/avc.c#L247
```c
static inline int avc_reclaim_node(void)
{
	struct avc_node *node;
	int hvalue, try, ecx;
	unsigned long flags;
	struct hlist_head *head;
	spinlock_t *lock;

	for (try = 0, ecx = 0; try < AVC_CACHE_SLOTS; try++) {
		hvalue = atomic_inc_return(&avc_cache.lru_hint) & (AVC_CACHE_SLOTS - 1); <<== Bounded assignment here
		head = &avc_cache.slots[hvalue];										 <<== This line
		lock = &avc_cache.slots_lock[hvalue];									 <<== This line
...
```
 
## Group 4
### This group contains a safely bounded variable index, which we can safely discard. Same as Group 2.

- https://github.com/torvalds/linux/blob/v3.19/security/selinux/avc.c#L692
```c
static noinline int avc_denied(u32 ssid, u32 tsid,
			 u16 tclass, u32 requested,
			 unsigned flags,
			 struct av_decision *avd)
{
	if (flags & AVC_STRICT)
		return -EACCES;

	if (selinux_enforcing && !(avd->flags & AVD_FLAGS_PERMISSIVE))
		return -EACCES;

	avc_update_node(AVC_CALLBACK_GRANT, requested, ssid,		  <<== This line
				tsid, tclass, avd->seqno);
	return 0;
}
```

- https://github.com/torvalds/linux/blob/v3.19/security/selinux/avc.c#L555
- https://github.com/torvalds/linux/blob/v3.19/security/selinux/avc.c#L556
```c
static int avc_update_node(u32 event, u32 perms, u32 ssid, u32 tsid, u16 tclass,
			   u32 seqno)
{
	int hvalue, rc = 0;
	unsigned long flag;
	struct avc_node *pos, *node, *orig = NULL;
	struct hlist_head *head;
	spinlock_t *lock;

	node = avc_alloc_node();
	if (!node) {
		rc = -ENOMEM;
		goto out;
	}

	/* Lock the target slot */
	hvalue = avc_hash(ssid, tsid, tclass);

	head = &avc_cache.slots[hvalue];							  <<== This line
	lock = &avc_cache.slots_lock[hvalue];						  <<== This line
...
```

## Group 5
### This group contains a safely bounded variable index, which we can safely discard. Same as Group 2.

- https://github.com/torvalds/linux/blob/v3.19/security/selinux/avc.c#L333
```c
static struct avc_node *avc_lookup(u32 ssid, u32 tsid, u16 tclass)
{
	struct avc_node *node;

	avc_cache_stats_incr(lookups);
	node = avc_search_node(ssid, tsid, tclass);					  <<== This line

	if (node)
		return node;

	avc_cache_stats_incr(misses);
	return NULL;
}
```

- https://github.com/torvalds/linux/blob/v3.19/security/selinux/avc.c#L303
```c
static inline struct avc_node *avc_search_node(u32 ssid, u32 tsid, u16 tclass)
{
	struct avc_node *node, *ret = NULL;
	int hvalue;
	struct hlist_head *head;

	hvalue = avc_hash(ssid, tsid, tclass);
	head = &avc_cache.slots[hvalue];							  <<== This line
```


## Group 6
### This group contains a variable index array access. It is accessed in a for loop where the index is bounded by a bookkeeping field(?) `len` of the same `sec_path` structure. This is a suspicious case, where it's easy to get right and hard to verify.

- https://github.com/torvalds/linux/blob/v3.19/security/selinux/xfrm.c#L268
```c
int selinux_xfrm_decode_session(struct sk_buff *skb, u32 *sid, int ckall)
{
	if (skb == NULL) {
		*sid = SECSID_NULL;
		return 0;
	}
	return selinux_xfrm_skb_sid_ingress(skb, sid, ckall);		  <<== This line
}
```

- https://github.com/torvalds/linux/blob/v3.19/security/selinux/xfrm.c#L237
```c
static int selinux_xfrm_skb_sid_ingress(struct sk_buff *skb,
					u32 *sid, int ckall)
{
	u32 sid_session = SECSID_NULL;
	struct sec_path *sp = skb->sp;

	if (sp) {
		int i;

		for (i = sp->len - 1; i >= 0; i--) {
			struct xfrm_state *x = sp->xvec[i];					  <<== This line
...
```


Related code for `struct sec_path`:
```c
// in include/net/xfrm.h
struct sec_path {
	atomic_t			refcnt;
	int					len;
	struct xfrm_state	*xvec[XFRM_MAX_DEPTH];
};
```
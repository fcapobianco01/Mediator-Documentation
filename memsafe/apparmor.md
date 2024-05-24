## Group 1
### This is an unsafe case, as the `resource` index is kernel input. The `limits` array can only be as large as 16.

Related hooks:
```c
apparmor_task_setrlimit
```

- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/resource.c#L108
```c
int aa_task_setrlimit(struct aa_profile *profile, struct task_struct *task,
		      unsigned int resource, struct rlimit *new_rlim)
{
	struct aa_profile *task_profile;
	int error = 0;

	rcu_read_lock();
	task_profile = aa_get_profile(aa_cred_profile(__task_cred(task)));
	rcu_read_unlock();

	/* TODO: extend resource control to handle other (non current)
	 * profiles.  AppArmor rules currently have the implicit assumption
	 * that the task is setting the resource of a task confined with
	 * the same profile.
	 */
	if (profile != task_profile ||
	    (profile->rlimits.mask & (1 << resource) &&
	     new_rlim->rlim_max > profile->rlimits.limits[resource].rlim_max))  <<== This line
		error = -EACCES;

	aa_put_profile(task_profile);

	return audit_resource(profile, resource, new_rlim->rlim_max, error);
}


struct aa_rlimit {
	unsigned int mask;
	struct rlimit limits[RLIM_NLIMITS];
};

#define RLIM_NLIMITS		16

```

## Group 2
### This is a (less) suspicious case, as `aa_profile_mode_names` is an array with the size of 4. The index here `profile->mode` is internally handled. I've checked all assignments of this field in apparmor, and they all look fine.

Related hooks:
```c
apparmor_getprocattr
```

- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/procattr.c#L40
```c
int aa_getprocattr(struct aa_profile *profile, char **string)
{
	char *str;
	int len = 0, mode_len = 0, ns_len = 0, name_len;
	const char *mode_str = aa_profile_mode_names[profile->mode];  <<== This line
```

## Group 3
### A safely bounded case by hardcoded limit of 16.

Related hooks:
```c
apparmor_setprocattr
```

- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/procattr.c#L140
```c
int aa_setprocattr_changehat(char *args, size_t size, int test)
{
	char *hat;
	u64 token;
	const char *hats[16];		/* current hard limit on # of names */
	int count = 0;

	hat = split_token_from_name(OP_CHANGE_HAT, args, &token);
	if (IS_ERR(hat))
		return PTR_ERR(hat);

	if (!hat && !token) {
		AA_ERROR("change_hat: Invalid input, NULL hat and NULL magic");
		return -EINVAL;
	}

	if (hat) {
		/* set up hat name vector, args guaranteed null terminated
		 * at args[size] by setprocattr.
		 *
		 * If there are multiple hat names in the buffer each is
		 * separated by a \0.  Ie. userspace writes them pre tokenized
		 */
		char *end = args + size;
		for (count = 0; (hat < end) && count < 16; ++count) {
			char *next = hat + strlen(hat) + 1;
			hats[count] = hat;                                    <<== This line
			hat = next;
		}
	}

	AA_DEBUG("%s: Magic 0x%llx Hat '%s'\n",
		 __func__, token, hat ? hat : NULL);

	return aa_change_hat(hats, count, token, test);
}
```


- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/capability.c#L79
- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/capability.c#L84
- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/capability.c#L95
- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/capability.c#L103
```c
static int audit_caps(struct aa_profile *profile, int cap, int error)
{
	struct audit_cache *ent;
	int type = AUDIT_APPARMOR_AUTO;
	struct common_audit_data sa;
	struct apparmor_audit_data aad = {0,};
	sa.type = LSM_AUDIT_DATA_CAP;
	sa.aad = &aad;
	sa.u.cap = cap;
	sa.aad->op = OP_CAPABLE;
	sa.aad->error = error;

	if (likely(!error)) {
		/* test if auditing is being forced */
		if (likely((AUDIT_MODE(profile) != AUDIT_ALL) &&
			   !cap_raised(profile->caps.audit, cap)))            <<== This line
			return 0;
		type = AUDIT_APPARMOR_AUDIT;
	} else if (KILL_MODE(profile) ||
		   cap_raised(profile->caps.kill, cap)) {                 <<== This line
		type = AUDIT_APPARMOR_KILL;
	} else if (cap_raised(profile->caps.quiet, cap) &&            <<== Why not this line?
		   AUDIT_MODE(profile) != AUDIT_NOQUIET &&
		   AUDIT_MODE(profile) != AUDIT_ALL) {
		/* quiet auditing */
		return error;
	}

	/* Do simple duplicate message elimination */
	ent = &get_cpu_var(audit_cache);
	if (profile == ent->profile && cap_raised(ent->caps, cap)) {  <<== This line
		put_cpu_var(audit_cache);
		if (COMPLAIN_MODE(profile))
			return complain_error(error);
		return error;
	} else {
		aa_put_profile(ent->profile);
		ent->profile = aa_get_profile(profile);
		cap_raise(ent->caps, cap);                                <<== This line
	}
	put_cpu_var(audit_cache);

	return aa_audit(type, profile, GFP_ATOMIC, &sa, audit_cb);
}
```

Related code:
```c
#define cap_raise(c, flag)  ((c).cap[CAP_TO_INDEX(flag)] |= CAP_TO_MASK(flag))
#define cap_raised(c, flag) ((c).cap[CAP_TO_INDEX(flag)] & CAP_TO_MASK(flag))

#define CAP_TO_INDEX(x)     ((x) >> 5)        /* 1 << 5 == bits in __u32 */
#define CAP_TO_MASK(x)      (1 << ((x) & 31)) /* mask for indexed __u32 */
```

## Group 4
### The variable index `index` here is architecture dependent, relies on the programmer to get it right. (Also seen in Tomoyo)

Related hooks:
```c
apparmor_file_open
apparmor_file_permission
apparmor_file_alloc_security
apparmor_mmap_file
apparmor_file_mprotect
apparmor_file_lock
apparmor_cred_alloc_blank
```

- https://github.com/torvalds/linux/blob/v3.19/include/linux/slab.h#L424
```c
static __always_inline void *kmalloc(size_t size, gfp_t flags)
{
	if (__builtin_constant_p(size)) {
		if (size > KMALLOC_MAX_CACHE_SIZE)
			return kmalloc_large(size, flags);
#ifndef CONFIG_SLOB
		if (!(flags & GFP_DMA)) {
			int index = kmalloc_index(size);

			if (!index)
				return ZERO_SIZE_PTR;

			return kmem_cache_alloc_trace(kmalloc_caches[index],  <<== This line
                              flags, size);
					flags, size);
		}
#endif
	}
	return __kmalloc(size, flags);
}
```

The index returned by `kmalloc_index` can be as large as 26. But `kmalloc_caches`, 
defined as global cache(?), is architecture dependent and can be as small as 12.
```c
struct kmem_cache *kmalloc_caches[KMALLOC_SHIFT_HIGH + 1];
```

## Group 5
### Same problem as in Group 4.

Related hooks:
```c
apparmor_path_link  
apparmor_path_unlink  
apparmor_path_symlink  
apparmor_path_mkdir
apparmor_path_rmdir
apparmor_path_mknod
apparmor_path_rename
apparmor_path_chmod
apparmor_path_chown
apparmor_path_truncate
apparmor_inode_getattr
```

- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/path.c#L218
```c
int aa_path_name(struct path *path, int flags, char **buffer, const char **name,
		 const char **info)
{
	char *buf, *str = NULL;
	int size = 256;
	int error;

	*name = NULL;
	*buffer = NULL;
	for (;;) {
		/* freed by caller */
		buf = kmalloc(size, GFP_KERNEL);                          <<== This line
```
- https://github.com/torvalds/linux/blob/v3.19/include/linux/slab.h#L424

## Group 6
### This is a safely bounded case. Bounding on `_KERNEL_CAPABILITY_U32S`.

Related hooks:
```c
apparmor_capget
```

- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/lsm.c#L131
```c
		*effective = cap_intersect(*effective, profile->caps.allow);  <<== This line
		*permitted = cap_intersect(*permitted, profile->caps.allow);  <<== But this line not reported?
```
- https://github.com/torvalds/linux/blob/v3.19/include/linux/capability.h#L129
```c
static inline kernel_cap_t cap_intersect(const kernel_cap_t a,
					 const kernel_cap_t b)
{
	kernel_cap_t dest;
	CAP_BOP_ALL(dest, a, b, &);
	return dest;
}


#define CAP_BOP_ALL(c, a, b, OP)                                    \
do {                                                                \
	unsigned __capi;                                            \
	CAP_FOR_EACH_U32(__capi) {                                  \
		c.cap[__capi] = a.cap[__capi] OP b.cap[__capi];     \
	}                                                           \
} while (0)

#define CAP_FOR_EACH_U32(__capi)  \
	for (__capi = 0; __capi < _KERNEL_CAPABILITY_U32S; ++__capi)
```
Only potential problem is `unsigned __capi` being unintialized? Looked up on StackOverflow (https://stackoverflow.com/a/6212973/4477913):
> External and static variables are initialized to zero by default, this is guaranteed. 

Not certain if macro variables falls into these cases, need double check.

## Group 7
### Same as the problem seen in Group 3.

Related hooks:
```c
apparmor_ptrace_access_check
apparmor_ptrace_traceme
apparmor_capable
```

- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/capability.c#L79
- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/capability.c#L84
- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/capability.c#L95
- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/capability.c#L103

The above are already seen in Group 3.

- https://github.com/torvalds/linux/blob/v3.19/security/apparmor/capability.c#L119
```c
static int profile_capable(struct aa_profile *profile, int cap)
{
	return cap_raised(profile->caps.allow, cap) ? 0 : -EPERM;
}
```
Same as the problem seen in Group 3.
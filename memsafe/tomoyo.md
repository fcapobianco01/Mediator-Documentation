## Group 1
### This group contains a safely bounded variable index, which we can safely discard.

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L596  
```c
int tomoyo_execute_permission(struct tomoyo_request_info *r,
			      const struct tomoyo_path_info *filename)
{
	/*
	 * Unlike other permission checks, this check is done regardless of
	 * profile mode settings in order to check for domain transition
	 * preference.
	 */
	r->type = TOMOYO_MAC_FILE_EXECUTE;
	r->mode = tomoyo_get_mode(r->domain->ns, r->profile, r->type);  <<== This line
	...
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L981
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L983
```c
int tomoyo_get_mode(const struct tomoyo_policy_namespace *ns, const u8 profile,
		    const u8 index)
{
	u8 mode;
	struct tomoyo_profile *p;

	if (!tomoyo_policy_loaded)
		return TOMOYO_CONFIG_DISABLED;
	p = tomoyo_profile(ns, profile);
	mode = p->config[index];									  <<== This line
	if (mode == TOMOYO_CONFIG_USE_DEFAULT)
		mode = p->config[tomoyo_index2category[index]
				 + TOMOYO_MAX_MAC_INDEX];						  <<== This line
	if (mode == TOMOYO_CONFIG_USE_DEFAULT)
		mode = p->default_config;
	return mode & 3;
}
```

Because `index` passed into `tomoyo_get_mode` is `TOMOYO_MAC_FILE_EXECUTE`, it 
will bound the variable index of `p->config`. Thus it is safe.


## Group 2
### The variable index `index` here is architecture dependent, relies on the programmer to get it right. Seen in all 3 LSMs.


https://github.com/torvalds/linux/blob/v3.19/include/linux/slab.h#L578

```c
static inline void *kzalloc(size_t size, gfp_t flags)
{
	return kmalloc(size, flags | __GFP_ZERO);  					  <<== This line
}
```

This line itself seems fine, not sure where the caller is.

https://github.com/torvalds/linux/blob/v3.19/include/linux/slab.h#L424
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

## Group 3
### There is no problem on these cases, the memory access is bounded by the for loop condition `i < TOMOYO_MAX_PATH_STAT`. Can safely discard.

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L180  
It has multiple definition sets, including:  
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L726
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L719
```c
    for (i = 0; i < TOMOYO_MAX_PATH_STAT; i++) {
    ...
		if (inode) {
			struct tomoyo_mini_stat *stat = &obj->stat[i];      <<==
            ...
			obj->stat_valid[i] = true;                          <<==
		}
        ...
	}
```

## Group 4
### Same as [Group 2](#group-2).

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/realpath.c#L265
```c
		buf = kmalloc(buf_len, GFP_NOFS);
```


## Group 5 
### This is a suspicious case (minor). 

I have checked all assignment locations of `r->mode` that *I can find*, 
which all seem to be using the `tomoyo_get_mode` function (safe). 
However, I cannot confirm I identified all `r->mode` assignments.

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/realpath.c#L265  

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2273
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2274
```c
void tomoyo_update_stat(const u8 index)
{
	tomoyo_stat_updated[index]++;                       	      <<== This line
	tomoyo_stat_modified[index] = get_seconds();        		  <<== This line
}
```
The two lines looks problematic with the argument `index`, but it doesn't look 
like it comes from `realpath.c:265`

## Group 6 
### This group contains a safely bounded variable index, which we can safely discard.

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L604
```c
int tomoyo_execute_permission(struct tomoyo_request_info *r,
			      const struct tomoyo_path_info *filename)
{
	...
	r->param.path.operation = TOMOYO_TYPE_EXECUTE;		 		  <<== Related assignment
	tomoyo_check_acl(r, tomoyo_check_path_acl);
	r->ee->transition = r->matched_acl && r->matched_acl->cond ?
		r->matched_acl->cond->transit : NULL;
	if (r->mode != TOMOYO_CONFIG_DISABLED)
		return tomoyo_audit_path_log(r);						  <<== This line
	return 0;
}
```

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L167
```c
static int tomoyo_audit_path_log(struct tomoyo_request_info *r)
{
	return tomoyo_supervisor(r, "file %s %s\n", tomoyo_path_keyword
				 [r->param.path.operation],					  	  <<== This line
				 r->param.path.filename->name);
}
```
`TOMOYO_TYPE_EXECUTE` is a constant bounded by `TOMOYO_MAX_PATH_OPERATION`.
```c
enum tomoyo_path_acl_index {
	TOMOYO_TYPE_EXECUTE,
	TOMOYO_TYPE_READ,
	TOMOYO_TYPE_WRITE,
	TOMOYO_TYPE_APPEND,
	TOMOYO_TYPE_UNLINK,
	TOMOYO_TYPE_GETATTR,
	TOMOYO_TYPE_RMDIR,
	TOMOYO_TYPE_TRUNCATE,
	TOMOYO_TYPE_SYMLINK,
	TOMOYO_TYPE_CHROOT,
	TOMOYO_TYPE_UMOUNT,
	TOMOYO_MAX_PATH_OPERATION
};

const char * const tomoyo_path_keyword[TOMOYO_MAX_PATH_OPERATION] = {
...
};
```

## Group 7
### This is a safe case. 
Although there are external definitions of macros and constants, they are available in the bitcode.
I suspect the report of positive is due to the bitwise-and operation in the `ACC_MODE` macro.

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/tomoyo.c#L135
```c
	return tomoyo_check_open_permission(domain, &bprm->file->f_path,
					    O_RDONLY);
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L738
```c
int tomoyo_check_open_permission(struct tomoyo_domain_info *domain,
				 struct path *path, const int flag)
{
	const u8 acc_mode = ACC_MODE(flag);							  <<== This line
	...
```

External (kernel) code:
```c
// include/linux/fs.h
#define ACC_MODE(x) ("\004\002\006\006"[(x)&O_ACCMODE])

// /usr/include/asm-generic/fcntl.h
#define O_ACCMODE	00000003
#define O_RDONLY	00000000
```

## Group 8
### This is a safe case. Variable index `hash_long(hash, TOMOYO_HASH_BITS)` is bounded.

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L549
```c
	e.domainname = tomoyo_get_name(domainname);
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/memory.c#L158
```c
const struct tomoyo_path_info *tomoyo_get_name(const char *name)
{
	struct tomoyo_name *ptr;
	unsigned int hash;
	int len;
	struct list_head *head;

	if (!name)
		return NULL;
	len = strlen(name) + 1;
	hash = full_name_hash((const unsigned char *) name, len - 1);
	head = &tomoyo_name_list[hash_long(hash, TOMOYO_HASH_BITS)];	<<== This line
	...
```

The variable access is bounded by the hashing functions. Related code below:
```c
#define TOMOYO_HASH_BITS  8
#define TOMOYO_MAX_HASH (1u<<TOMOYO_HASH_BITS)

struct list_head tomoyo_name_list[TOMOYO_MAX_HASH];

#define hash_long(val, bits) hash_32(val, bits)
static inline u32 hash_32(u32 val, unsigned int bits)
{
	u32 hash = val * GOLDEN_RATIO_PRIME_32;
	return hash >> (32 - bits);
}
```

## Group 9
### This is a safe case. Variable index `operation` is bounded from the input argument `TOMOYO_TYPE_READ`.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L759
```c
			error = tomoyo_path_permission(&r, TOMOYO_TYPE_READ,
						       &buf);					  		  <<== This line
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L563
```c
static int tomoyo_path_permission(struct tomoyo_request_info *r, u8 operation,
				  const struct tomoyo_path_info *filename)
{
	int error;

	r->type = tomoyo_p2mac[operation];							  <<== This line
	r->mode = tomoyo_get_mode(r->domain->ns, r->profile, r->type);
```

## Group 10
### This is a safe case. Variable index `i` is bounded by the for loop condition `ARRAY_SIZE(tomoyo_callback)`.

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L1978
```c
static void tomoyo_add_entry(struct tomoyo_domain_info *domain, char *header)
{
	...
	if (!tomoyo_write_domain2(domain->ns, &domain->acl_info_list, buffer,	<<== This line
				  false))
		tomoyo_update_stat(TOMOYO_STAT_POLICY_UPDATES);
	...
}
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L1124
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L1126
```c
static int tomoyo_write_domain2(struct tomoyo_policy_namespace *ns,
				struct list_head *list, char *data,
				const bool is_delete)
{
	struct tomoyo_acl_param param = {
		.ns = ns,
		.list = list,
		.data = data,
		.is_delete = is_delete,
	};
	static const struct {
		const char *keyword;
		int (*write) (struct tomoyo_acl_param *);
	} tomoyo_callback[5] = {
		{ "file ", tomoyo_write_file },
		{ "network inet ", tomoyo_write_inet_network },
		{ "network unix ", tomoyo_write_unix_network },
		{ "misc ", tomoyo_write_misc },
		{ "task ", tomoyo_write_task },
	};
	u8 i;

	for (i = 0; i < ARRAY_SIZE(tomoyo_callback); i++) {
		if (!tomoyo_str_starts(&param.data,
				       tomoyo_callback[i].keyword))			      <<== This line
			continue;
		return tomoyo_callback[i].write(&param);			      <<== This line
	}
	return -EINVAL;
}
```

The `ARRAY_SIZE` macro is defined as:
```c
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]) + __must_be_array(arr))
```


## Group 11
### These are actually two separate cases. Both of them are safe.

The first case is safe because the variable `pref` is bounded by `TOMOYO_MAX_PREF` which is larger than `TOMOYO_PREF_MAX_LEARNING_ENTRY`.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L1073
```c
	if (count < tomoyo_profile(domain->ns, domain->profile)->
	    pref[TOMOYO_PREF_MAX_LEARNING_ENTRY])					  <<== This line
```

The next case is safe because the array `profile_ptr`'s size is TOMOYO_MAX_PROFILES(256), and the index `profile` is an `u8`.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L531
```c
struct tomoyo_profile *tomoyo_profile(const struct tomoyo_policy_namespace *ns,
				      const u8 profile)
{
	static struct tomoyo_profile tomoyo_null_profile;
	struct tomoyo_profile *ptr = ns->profile_ptr[profile];		  <<== This line
	if (!ptr)
		ptr = &tomoyo_null_profile;
	return ptr;
}
```

## Group 12
### Same as [Group 11](#group-11).
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L332
```c
	p = tomoyo_profile(ns, profile);							  <<== Reported this line
	if (tomoyo_log_count >= p->pref[TOMOYO_PREF_MAX_AUDIT_LOG])   <<== Maybe should be this line?
		return false;
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L531

## Group 13
### Similar to [Group 1](#group-1).
The variable `index` is coming from `index` in `tomoyo_init_request_info` function. 
This `index` is not always obviously bounded.  
***TODO: Needs further confirmation.***

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L1010
```c
int tomoyo_init_request_info(struct tomoyo_request_info *r,
			     struct tomoyo_domain_info *domain, const u8 index)
{
	u8 profile;
	memset(r, 0, sizeof(*r));
	if (!domain)
		domain = tomoyo_domain();
	r->domain = domain;
	profile = domain->profile;
	r->profile = profile;
	r->type = index;
	r->mode = tomoyo_get_mode(domain->ns, profile, index);		  <<== This line
	return r->mode;
}
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L981
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L983
```c
int tomoyo_get_mode(const struct tomoyo_policy_namespace *ns, const u8 profile,
		    const u8 index)
{
	u8 mode;
	struct tomoyo_profile *p;

	if (!tomoyo_policy_loaded)
		return TOMOYO_CONFIG_DISABLED;
	p = tomoyo_profile(ns, profile);
	mode = p->config[index];									  <<== This line
	if (mode == TOMOYO_CONFIG_USE_DEFAULT)
		mode = p->config[tomoyo_index2category[index]			  <<== This line
				 + TOMOYO_MAX_MAC_INDEX];
	if (mode == TOMOYO_CONFIG_USE_DEFAULT)
		mode = p->default_config;
	return mode & 3;
}
```


## Group 14
### This is a safe case. 

The variable index `domain->group` is `u8`, same as the array size of `acl_group`.

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/environ.c#L61
```c
	do {
		tomoyo_check_acl(r, tomoyo_check_env_acl);				  <<== This line
		error = tomoyo_audit_env_log(r);
	} while (error == TOMOYO_RETRY_REQUEST);
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L179
```c
	if (!retried) {
		retried = true;
		list = &domain->ns->acl_group[domain->group];			  <<== This line
		goto retry;
	}
```

## Group 15
### Same as [Group 14](#group-14).
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L571
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L179

## Group 16
### This is a safe case.
`r` and `m` are safely bounded by the `bool` type and the short circuit condition of `m < 11`.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L159
```c
	tomoyo_convert_time(get_seconds(), &stamp);					  <<== This line
```

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L112
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L115
```c
void tomoyo_convert_time(time_t time, struct tomoyo_time *stamp)
{
	static const u16 tomoyo_eom[2][12] = {
		{ 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365 },
		{ 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366 }
	};
	u16 y;
	u8 m;
	bool r;
	stamp->sec = time % 60;
	time /= 60;
	stamp->min = time % 60;
	time /= 60;
	stamp->hour = time % 24;
	time /= 24;
	for (y = 1970; ; y++) {
		const unsigned short days = (y & 3) ? 365 : 366;
		if (time < days)
			break;
		time -= days;
	}
	r = (y & 3) == 0;
	for (m = 0; m < 11 && time >= tomoyo_eom[r][m]; m++)		  <<== This line
		;
	if (m)
		time -= tomoyo_eom[r][m - 1];							  <<== This line
	stamp->year = y;
	stamp->month = ++m;
	stamp->day = ++time;
}
```

## Group 17
### This is a safe case, similar to [Group 1](#group-1). However, the assignment of `r->type` is not obviously bounded and needs comprehensive manual check.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L564
```c
static int tomoyo_path_permission(struct tomoyo_request_info *r, u8 operation,
				  const struct tomoyo_path_info *filename)
{
	int error;

	r->type = tomoyo_p2mac[operation];
	r->mode = tomoyo_get_mode(r->domain->ns, r->profile, r->type);	  <<== This line
	if (r->mode == TOMOYO_CONFIG_DISABLED)
		return 0;
	r->param_type = TOMOYO_TYPE_PATH_ACL;
	r->param.path.filename = filename;
	r->param.path.operation = operation;
	do {
		tomoyo_check_acl(r, tomoyo_check_path_acl);
		error = tomoyo_audit_path_log(r);
	} while (error == TOMOYO_RETRY_REQUEST);
	return error;
}
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L981
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L983
```c
int tomoyo_get_mode(const struct tomoyo_policy_namespace *ns, const u8 profile,
		    const u8 index)
{
	u8 mode;
	struct tomoyo_profile *p;

	if (!tomoyo_policy_loaded)
		return TOMOYO_CONFIG_DISABLED;
	p = tomoyo_profile(ns, profile);
	mode = p->config[index];
	if (mode == TOMOYO_CONFIG_USE_DEFAULT)
		mode = p->config[tomoyo_index2category[index]
				 + TOMOYO_MAX_MAC_INDEX];
	if (mode == TOMOYO_CONFIG_USE_DEFAULT)
		mode = p->default_config;
	return mode & 3;
}
```

## Group 18
### Same as [Group 11](#group-11).
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L980
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L531

## Group 19
### A related case of [Group 17](#group-17). 

The variable index `operation`'s all incoming sources are bounded. Manual inspection required for this case.

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L762
```c
static int tomoyo_path_permission(struct tomoyo_request_info *r, u8 operation,
				  const struct tomoyo_path_info *filename)
{
	int error;

	r->type = tomoyo_p2mac[operation];							  <<== This line
	r->mode = tomoyo_get_mode(r->domain->ns, r->profile, r->type);
	if (r->mode == TOMOYO_CONFIG_DISABLED)
		return 0;
	r->param_type = TOMOYO_TYPE_PATH_ACL;
	r->param.path.filename = filename;
	r->param.path.operation = operation;
	do {
		tomoyo_check_acl(r, tomoyo_check_path_acl);
		error = tomoyo_audit_path_log(r);
	} while (error == TOMOYO_RETRY_REQUEST);
	return error;
}
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L563

## Group 20
### This is a safe case. 

The macro `__ismask` works on `char` types and the array size of `_ctype` is 256. 

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L774
```c
			j = 0;
			c = *pattern;
			if (c == '$') {
				while (isdigit(filename[j]))
					j++;
			} else if (c == 'X') {
				while (isxdigit(filename[j]))
					j++;
			} else if (c == 'A') {
				while (tomoyo_alphabet_char(filename[j]))
					j++;
			}
			for (i = 1; i <= j; i++) {
				if (tomoyo_file_matches_pattern2(
						    filename + i, filename_end,
						    pattern + 1, pattern_end))
					return true;
			}
			return false; /* Not matched or bad pattern. */
```

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L718
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L722
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L764
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L767
```c
static bool tomoyo_file_matches_pattern2(const char *filename,
					 const char *filename_end,
					 const char *pattern,
					 const char *pattern_end)
{
		switch (*pattern) {
		...
		case '+':
			if (!isdigit(c))									  <<== This line
				return false;
			break;
		case 'x':
			if (!isxdigit(c))									  <<== This line
				return false;
			break;
		default:
			j = 0;
			c = *pattern;
			if (c == '$') {
				while (isdigit(filename[j]))					  <<== This line
					j++;
			} else if (c == 'X') {
				while (isxdigit(filename[j]))					  <<== This line
					j++;
		...
}
```

Kernel code: 
```c
// include/linux/ctype.h
extern const unsigned char _ctype[];

#define __ismask(x) (_ctype[(int)(unsigned char)(x)])

#define isdigit(c)	((__ismask(c)&(_D)) != 0)
#define isxdigit(c)	((__ismask(c)&(_D|_X)) != 0)

// include/linux/ctype.c
const unsigned char _ctype[] = {
_C,_C,_C,_C,_C,_C,_C,_C,				/* 0-7 */
_C,_C|_S,_C|_S,_C|_S,_C|_S,_C|_S,_C,_C,			/* 8-15 */
_C,_C,_C,_C,_C,_C,_C,_C,				/* 16-23 */
_C,_C,_C,_C,_C,_C,_C,_C,				/* 24-31 */
_S|_SP,_P,_P,_P,_P,_P,_P,_P,				/* 32-39 */
_P,_P,_P,_P,_P,_P,_P,_P,				/* 40-47 */
_D,_D,_D,_D,_D,_D,_D,_D,				/* 48-55 */
_D,_D,_P,_P,_P,_P,_P,_P,				/* 56-63 */
_P,_U|_X,_U|_X,_U|_X,_U|_X,_U|_X,_U|_X,_U,		/* 64-71 */
_U,_U,_U,_U,_U,_U,_U,_U,				/* 72-79 */
_U,_U,_U,_U,_U,_U,_U,_U,				/* 80-87 */
_U,_U,_U,_P,_P,_P,_P,_P,				/* 88-95 */
_P,_L|_X,_L|_X,_L|_X,_L|_X,_L|_X,_L|_X,_L,		/* 96-103 */
_L,_L,_L,_L,_L,_L,_L,_L,				/* 104-111 */
_L,_L,_L,_L,_L,_L,_L,_L,				/* 112-119 */
_L,_L,_L,_P,_P,_P,_P,_C,				/* 120-127 */
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,			/* 128-143 */
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,			/* 144-159 */
_S|_SP,_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,	/* 160-175 */
_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,_P,	/* 176-191 */
_U,_U,_U,_U,_U,_U,_U,_U,_U,_U,_U,_U,_U,_U,_U,_U,	/* 192-207 */
_U,_U,_U,_U,_U,_U,_U,_P,_U,_U,_U,_U,_U,_U,_U,_L,	/* 208-223 */
_L,_L,_L,_L,_L,_L,_L,_L,_L,_L,_L,_L,_L,_L,_L,_L,	/* 224-239 */
_L,_L,_L,_L,_L,_L,_L,_P,_L,_L,_L,_L,_L,_L,_L,_L};	/* 240-255 */

EXPORT_SYMBOL(_ctype);
```

## Group 21
### Same as [Group 5](#group-5).
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/realpath.c#L1980

*This line does not exist.*

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2273
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2274
```c
static unsigned int tomoyo_stat_updated[TOMOYO_MAX_POLICY_STAT];
static unsigned int tomoyo_stat_modified[TOMOYO_MAX_POLICY_STAT];

void tomoyo_update_stat(const u8 index)
{
	tomoyo_stat_updated[index]++;								  <<== This line
	tomoyo_stat_modified[index] = get_seconds();		          <<== This line
}
```


## Group 22
### Same as [Group 20](#group-20).

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L813
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L718
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L722
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L764
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L767

## Group 23
### Same as [Group 2](#group-2).

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L1967
https://github.com/torvalds/linux/blob/v3.19/include/linux/slab.h#L424

## Group 24
### Same as [Group 20](#group-20).

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L743
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L718
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L722
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L764
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L767

## Group 25
### Same as [Group 14](#group-14).

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L600
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L179

## Group 26
### Same as [Group 2](#group-2).

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L153
https://github.com/torvalds/linux/blob/v3.19/include/linux/slab.h#L424

## Group 27
### 

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L171
```c

```

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L773
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L774
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L775
```c
bool tomoyo_condition(struct tomoyo_request_info *r,
		      const struct tomoyo_condition *cond)
{
	u32 i;
	unsigned long min_v[2] = { 0, 0 };
	unsigned long max_v[2] = { 0, 0 };
	const struct tomoyo_condition_element *condp;
	const struct tomoyo_number_union *numbers_p;
	const struct tomoyo_name_union *names_p;
	const struct tomoyo_argv *argv;
	const struct tomoyo_envp *envp;
	struct tomoyo_obj_info *obj;
	u16 condc;
	u16 argc;
	u16 envc;
	struct linux_binprm *bprm = NULL;
	if (!cond)
		return true;
	condc = cond->condc;
	argc = cond->argc;
	envc = cond->envc;
	obj = r->obj;
	if (r->ee)
		bprm = r->ee->bprm;
	if (!bprm && (argc || envc))
		return false;
	condp = (struct tomoyo_condition_element *) (cond + 1);
	numbers_p = (const struct tomoyo_number_union *) (condp + condc);
	names_p = (const struct tomoyo_name_union *)
		(numbers_p + cond->numbers_count);								  <<== This line
	argv = (const struct tomoyo_argv *) (names_p + cond->names_count);	  <<== This line
	envp = (const struct tomoyo_envp *) (argv + argc);					  <<== This line
```

***TODO: Type casting safety?***

The other cases below are bounded inside the same function.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L965
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L967
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L1017
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L1018
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L1032
```c
	...
	unsigned long min_v[2] = { 0, 0 };
	unsigned long max_v[2] = { 0, 0 };
	...
		bool is_bitop[2] = { false, false };

		for (j = 0; j < 2; j++) {
			...
			max_v[j] = value;										  <<== This line
			min_v[j] = value;					  					  <<== This line

			...
				is_bitop[j] = true;									  <<== This line

```

## Group 28
### Same as [Group 11](#group-11).

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L818
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L519

## Group 29
### Same as [Group 1](#group-1).

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L604
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L981
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L983

## Group 30
### Same as [Group 6](#group-6). Safe case, but needs manual inspection of incoming source of variables.

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L572
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L167

## Group 31
### This is a suspicious case (minor). 

I have checked all assignment locations of `r->mode` that *I can find*, 
which all seem to be using the `tomoyo_get_mode` function (safe). 
However, I cannot confirm I identified all `r->mode` assignments.

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L251
```c
	header = tomoyo_print_header(r);
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L167
```c
	pos = snprintf(buffer, tomoyo_buffer_len - 1,
		       "#%04u/%02u/%02u %02u:%02u:%02u# profile=%u mode=%s "
		       "granted=%s (global-pid=%u) task={ pid=%u ppid=%u "
		       "uid=%u gid=%u euid=%u egid=%u suid=%u sgid=%u "
		       "fsuid=%u fsgid=%u }", stamp.year, stamp.month,
		       stamp.day, stamp.hour, stamp.min, stamp.sec, r->profile,
		       tomoyo_mode[r->mode], tomoyo_yesno(r->granted), gpid,	<<== This line
		       tomoyo_sys_getpid(), tomoyo_sys_getppid(),
		       from_kuid(&init_user_ns, current_uid()),
		       from_kgid(&init_user_ns, current_gid()),
		       from_kuid(&init_user_ns, current_euid()),
		       from_kgid(&init_user_ns, current_egid()),
		       from_kuid(&init_user_ns, current_suid()),
		       from_kgid(&init_user_ns, current_sgid()),
		       from_kuid(&init_user_ns, current_fsuid()),
		       from_kgid(&init_user_ns, current_fsgid()));
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L189
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L187

This above two are the same as [Group 3](#group-3).


## Group 32
### There is no way to confirm the safety of this case. 

The `argc` and `argv` are assigned in `tomoyo_condition`, and there are pointer casts. 
I can't even manually verify this case. 

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L1092
```c
bool tomoyo_condition(struct tomoyo_request_info *r,
		      const struct tomoyo_condition *cond)
{
	u32 i;
	unsigned long min_v[2] = { 0, 0 };
	unsigned long max_v[2] = { 0, 0 };
	const struct tomoyo_condition_element *condp;
	const struct tomoyo_number_union *numbers_p;
	const struct tomoyo_name_union *names_p;
	const struct tomoyo_argv *argv;
	const struct tomoyo_envp *envp;
	struct tomoyo_obj_info *obj;
	u16 condc;
	u16 argc;
	u16 envc;
	struct linux_binprm *bprm = NULL;
	if (!cond)
		return true;
	condc = cond->condc;
	argc = cond->argc;
	envc = cond->envc;
	obj = r->obj;
	if (r->ee)
		bprm = r->ee->bprm;
	if (!bprm && (argc || envc))
		return false;
	condp = (struct tomoyo_condition_element *) (cond + 1);
	numbers_p = (const struct tomoyo_number_union *) (condp + condc);
	names_p = (const struct tomoyo_name_union *)
		(numbers_p + cond->numbers_count);
	argv = (const struct tomoyo_argv *) (names_p + cond->names_count);
	envp = (const struct tomoyo_envp *) (argv + argc);
	...
	...
		return tomoyo_scan_bprm(r->ee, argc, argv, envc, envp);
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L192
```c
static bool tomoyo_scan_bprm(struct tomoyo_execve *ee,
			     const u16 argc, const struct tomoyo_argv *argv,
			     const u16 envc, const struct tomoyo_envp *envp)
{
	...
		for (i = 0; i < argc; i++) {
			if (checked[i])
				continue;
			/*
			 * Return true only if all unchecked indexes in
			 * bprm->argv[] are not matched.
			 */
			if (argv[i].is_not)									  <<== This line
				continue;
			result = false;
			break;
		}
```

## Group 33
### Same as [Group 20](#group-20).

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L824
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L718
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L722
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L764
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L767

## Group 34
### Same as [Group 3](#group-3).

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L919
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L719
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L726

## Group 35
### This is a safe case.

All the indices are bounded by the for-loop conditions.

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L470
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L351
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L349
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L347
```c
void tomoyo_init_policy_namespace(struct tomoyo_policy_namespace *ns)
{
	unsigned int idx;
	for (idx = 0; idx < TOMOYO_MAX_ACL_GROUPS; idx++)
		INIT_LIST_HEAD(&ns->acl_group[idx]);						  <<== This line
	for (idx = 0; idx < TOMOYO_MAX_GROUP; idx++)
		INIT_LIST_HEAD(&ns->group_list[idx]);						  <<== This line
	for (idx = 0; idx < TOMOYO_MAX_POLICY; idx++)
		INIT_LIST_HEAD(&ns->policy_list[idx]);						  <<== This line
	ns->profile_version = 20110903;
	tomoyo_namespace_enabled = !list_empty(&tomoyo_namespace_list);
	list_add_tail_rcu(&ns->namespace_list, &tomoyo_namespace_list);
}
```

## Group 36
### Similar as [Group 5](#group-5).

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2014
```c
int tomoyo_supervisor(struct tomoyo_request_info *r, const char *fmt, ...)
{
	va_list args;
	int error;
	int len;
	static unsigned int tomoyo_serial;
	struct tomoyo_query entry = { };
	bool quota_exceeded = false;
	va_start(args, fmt);
	len = vsnprintf((char *) &len, 1, fmt, args) + 1;
	va_end(args);
	/* Write /sys/kernel/security/tomoyo/audit. */
	va_start(args, fmt);
	tomoyo_write_log2(r, len, fmt, args);
	va_end(args);
	/* Nothing more to do if granted. */
	if (r->granted)
		return 0;
	if (r->mode)
		tomoyo_update_stat(r->mode); 							  <<== This line
```
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2273
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2274
```c
void tomoyo_update_stat(const u8 index)
{
	tomoyo_stat_updated[index]++;								  <<== This line
	tomoyo_stat_modified[index] = get_seconds();				  <<== This line
}
```

## Group 37
### There is no way to confirm the safety of this case. 

Specifically, the `r->type` going into `tomoyo_get_audit` is not obviously bounded.
I manually checked the incoming sources of all `r->type` that *I can find*. 
For all the network hooks (one example below), the `sock` comes from the kernel,
and late decides the `address.protocol`.

***TODO: Needs further confirmation from kernel code.***

```c
static int tomoyo_socket_listen(struct socket *sock, int backlog)
{
	return tomoyo_socket_listen_permission(sock);
}

static int tomoyo_unix_entry(const struct tomoyo_addr_info *address)
{
	...
	const u8 type = tomoyo_unix2mac[address->protocol][address->operation];

	if (type && tomoyo_init_request_info(&r, NULL, type)
	    != TOMOYO_CONFIG_DISABLED) {
	...
```


https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L364
```c
void tomoyo_write_log2(struct tomoyo_request_info *r, int len, const char *fmt,
		       va_list args)
{
	char *buf;
	struct tomoyo_log *entry;
	bool quota_exceeded = false;
	if (!tomoyo_get_audit(r->domain->ns, r->profile, r->type,	  <<== This line
			      r->matched_acl, r->granted))
```

https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L338
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L327
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L340
```c
static bool tomoyo_get_audit(const struct tomoyo_policy_namespace *ns,
			     const u8 profile, const u8 index,
			     const struct tomoyo_acl_info *matched_acl,
			     const bool is_granted)
{
	u8 mode;
	const u8 category = tomoyo_index2category[index] +			  <<== This line
		TOMOYO_MAX_MAC_INDEX;
	struct tomoyo_profile *p;
	if (!tomoyo_policy_loaded)
		return false;
	p = tomoyo_profile(ns, profile);
	if (tomoyo_log_count >= p->pref[TOMOYO_PREF_MAX_AUDIT_LOG])
		return false;
	if (is_granted && matched_acl && matched_acl->cond &&
	    matched_acl->cond->grant_log != TOMOYO_GRANTLOG_AUTO)
		return matched_acl->cond->grant_log == TOMOYO_GRANTLOG_YES;
	mode = p->config[index];									  <<== This line
	if (mode == TOMOYO_CONFIG_USE_DEFAULT)
		mode = p->config[category];								  <<== This line
	if (mode == TOMOYO_CONFIG_USE_DEFAULT)
		mode = p->default_config;
	if (is_granted)
		return mode & TOMOYO_CONFIG_WANT_GRANT_LOG;
	return mode & TOMOYO_CONFIG_WANT_REJECT_LOG;
}
```
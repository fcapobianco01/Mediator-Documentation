Hook function 

### `tomoyo_bprm_check_security`

1. 
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L596  
It has multiple definition sets, including:  
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L981
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L983


2. 
https://github.com/torvalds/linux/blob/v3.19/include/linux/slab.h#L578

```
static inline void *kzalloc(size_t size, gfp_t flags)
{
	return kmalloc(size, flags | __GFP_ZERO);  <<==
}
```

This line itself seems find, not sure where the caller is.

https://github.com/torvalds/linux/blob/v3.19/include/linux/slab.h#L424
```
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

			return kmem_cache_alloc_trace(kmalloc_caches[index],  <<==
					flags, size);
		}
#endif
	}
	return __kmalloc(size, flags);
}
```

The index returned by `kmalloc_index` can be as large as 26. But `kmalloc_caches`, 
defined as global cache(?), is architecture dependent and can be as small as 12.
```
struct kmem_cache *kmalloc_caches[KMALLOC_SHIFT_HIGH + 1];
```





3. 
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L180  
It has multiple definition sets, including:  
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L726
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L719
```
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
There is no problem on these cases, the memory access is bounded by the for loop 
condition `TOMOYO_MAX_PATH_STAT`

4. 
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/realpath.c#L265
```
		buf = kmalloc(buf_len, GFP_NOFS);
```
Source of problem 2?

https://github.com/torvalds/linux/blob/v3.19/include/linux/slab.h#L424

Saw from problem 2.



5. 
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/realpath.c#L265  
It has multiple definition sets, including:  
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2273
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2274
```
void tomoyo_update_stat(const u8 index)
{
	tomoyo_stat_updated[index]++;                       <<==
	tomoyo_stat_modified[index] = get_seconds();        <<==
}
```
The two lines looks problematic with the argument `index`, but it doesn't look 
like it comes from `realpath.c:265`

6. 
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L604
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L167

7.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/tomoyo.c#L135
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L738

8.https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L549
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/memory.c#L158

9.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L759
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L563

10.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L1978
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L1124
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L1126
11.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L1073
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L531

12.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L332
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L531

13.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L1010
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L981
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L983

14.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/environ.c#L61
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L179

15.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L571
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L179

16.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L159
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L112
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L115

17.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L564
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L981
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L983

18.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L980
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L531

19.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L762
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L563

20.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L774
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L718
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L722
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L764
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L767

21.https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/realpath.c#L1980
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2273
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2274

22.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L813
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L718
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L722
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L764
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L767

23.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L1967
https://github.com/torvalds/linux/blob/v3.19/include/linux/slab.h#L424

24.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L743
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L718
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L722
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L764
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L767

25.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L600
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L179

26.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L153
https://github.com/torvalds/linux/blob/v3.19/include/linux/slab.h#L424

27.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L171
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L773
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L774
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L775
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L965
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L967
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L1017
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L1018
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L1032

28.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L818
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L519

29.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L604
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L981
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L983

30.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L572
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/file.c#L167

31.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L251
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L167
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L189
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L187


32.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L1092
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L192
33.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L824
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L718
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L722
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L764
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/util.c#L767

34.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L919
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L726
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/condition.c#L719

35.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/domain.c#L470
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L351
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L349
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L347
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L

36.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2014
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2273
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/common.c#L2274

37.
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L364
It has multiple definition sets, including:
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L338
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L327
https://github.com/torvalds/linux/blob/v3.19/security/tomoyo/audit.c#L340
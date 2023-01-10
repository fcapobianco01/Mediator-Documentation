| Source (name [type])          | Field (index [id]) | Source Location                    | Label at Source             |
|-------------------------------|--------------------|------------------------------------|-----------------------------|
| current                       |                    | security/selinux/hooks.c:1706      | subject, dynamic, external  |
| dir                           |                    | security/selinux/hooks.c:2782      | object, dynamic, input      |
| 7 [SECCLASS_DIR]              |                    | security/selinux/hooks.c:2784      | operation, static, mediator |
| 1048576 [DIR__ADD_NAME]       |                    | security/selinux/hooks.c:1723      | operation, static, mediator |
| 8388608 [DIR__SEARCH]         |                    | security/selinux/hooks.c:1723      | operation, static, mediator |
| 8 [FILE__CREATE]              |                    | security/selinux/hooks.c:1735      | operation, static, mediator |
| 128 [FILESYSTEM__ASSOCIATE]   |                    | security/selinux/hooks.c:1741      | operation, static, mediator |
| 12 [PAGE_SHIFT]               |                    | include/asm-generic/getorder.h:18  | all, static, external       |
| 64 [BITS_PER_LONG]            |                    | include/asm-generic/getorder.h:19  | all, static, external       |
| 8192 [KMALLOC_MAX_CACHE_SIZE] |                    | include/linux/slab.h:415           | all, static, external       |
| 16 [ZERO_SIZE_PTR]            |                    | include/linux/slab.h:422           | all, static, external       |
| 1 [GFP_DMA]                   |                    | include/linux/slab.h:418           | all, static, external       |
| 8 [KMALLOC_MIN_SIZE]          |                    | include/linux/slab.h:252           | all, static, external       |
| 64 [KMALLOC_MIN_SIZE]         |                    | include/linux/slab.h:255           | all, static, external       |
| 192 [KMALLOC_MIN_SIZE]        |                    | include/linux/slab.h:257           | all, static, external       |
| 3 [KMALLOC_SHIFT_LOW]         |                    | include/linux/slab.h:253           | all, static, external       |
| 32768 [__GFP_ZERO]            |                    | include/linux/slab.h:578           | all, static, external       |
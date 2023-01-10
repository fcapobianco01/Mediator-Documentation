| Source (name [type])          | Field (index [id]) | Source Location                   | Label at Source             |
|-------------------------------|--------------------|-----------------------------------|-----------------------------|
| current                       |                    | security/selinux/hooks.c:218      | subject, dynamic, external  |
| current                       |                    | security/selinux/hooks.c:5298     | subject, dynamic, external  |
| shp                           |                    | security/selinux/hooks.c:5291     | object, dynamic, input      |
| 1 [SHM__CREATE]               |                    | security/selinux/hooks.c:5308     | operation, static, mediator |
| 12 [PAGE_SHIFT]               |                    | include/asm-generic/getorder.h:18 | all, static, external       |
| 64 [BITS_PER_LONG]            |                    | include/asm-generic/getorder.h:19 | all, static, external       |
| 8192 [KMALLOC_MAX_CACHE_SIZE] |                    | include/linux/slab.h:415          | all, static, external       |
| 16 [ZERO_SIZE_PTR]            |                    | include/linux/slab.h:422          | all, static, external       |
| 1 [GFP_DMA]                   |                    | include/linux/slab.h:418          | all, static, external       |
| 8 [KMALLOC_MIN_SIZE]          |                    | include/linux/slab.h:252          | all, static, external       |
| 64 [KMALLOC_MIN_SIZE]         |                    | include/linux/slab.h:255          | all, static, external       |
| 192 [KMALLOC_MIN_SIZE]        |                    | include/linux/slab.h:257          | all, static, external       |
| 3 [KMALLOC_SHIFT_LOW]         |                    | include/linux/slab.h:253          | all, static, external       |
| 32768 [__GFP_ZERO]            |                    | include/linux/slab.h:578          | all, static, external       |
| 0 [_THIS_IP_]                 |                    | include/linux/rcupdate.h:418      | all, static, external       |
| 1 [_THIS_IP_]                 |                    | include/linux/rcupdate.h:423      | all, static, external       |
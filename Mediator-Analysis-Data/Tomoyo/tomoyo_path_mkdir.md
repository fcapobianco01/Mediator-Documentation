| Source  [type]                  | Field (index [id]) | Source Location                   | Label at Source             |
|---------------------------------|--------------------|-----------------------------------|-----------------------------|
| 1 [TOMOYO_TYPE_MKDIR]           |                    | security/tomoyo/tomoyo.c:192      | operation, static, mediator |
| path                            |                    | security/tomoyo/tomoyo.c:188      | object, dynamic, input      |
| dentry                          |                    | security/tomoyo/tomoyo.c:188      | object, dynamic, input      |
| mode                            |                    | security/tomoyo/tomoyo.c:188      | operation, dynamic, input   |
| 0 [TOMOYO_CONFIG_DISABLED]      |                    | security/tomoyo/file.c:702        | all, static, mediator       |
| 3 [TOMOYO_CONFIG_ENFORCING]     |                    | security/tomoyo/file.c:721        | all, static, mediator       |
| 2 [TOMOYO_TYPE_PATH_NUMBER_ACL] |                    | security/tomoyo/file.c:710        | all, static, mediator       |
| 1 [TOMOYO_TYPE_MKDIR]           |                    | security/tomoyo/file.c:708        | operation, static, mediator |
| '\0'                            |                    | security/tomoyo/realpath.c:269    | all, static, mediator       |
| 256                             |                    | security/tomoyo/realpath.c:125    | all, static, mediator       |
| '/'                             |                    | security/tomoyo/realpath.c:158    | all, static, mediator       |
| '/'                             |                    | security/tomoyo/realpath.c:127    | all, static, mediator       |
| '/'                             |                    | security/tomoyo/realpath.c:130    | all, static, mediator       |
| "dev(%u,%u):"                   |                    | security/tomoyo/realpath.c:185    | all, static, mediator       |
| ':'                             |                    | security/tomoyo/realpath.c:203    | all, static, mediator       |
| current                         |                    | security/tomoyo/common.h:1139     | subject, dynamic, external  |
| current                         |                    | security/tomoyo/common.h:1124     | subject, dynamic, external  |
| 4095 [S_IALLUGO]                |                    | security/tomoyo/tomoyo.c:364      | all, static, external       |
| 0 [enum]                        |                    | include/linux/pid.h:6             | all, static, external       |
| 12 [PAGE_SHIFT]                 |                    | include/asm-generic/getorder.h:18 | all, static, external       |
| 64 [BITS_PER_LONG]              |                    | include/asm-generic/getorder.h:19 | all, static, external       |
| 8192 [KMALLOC_MAX_CACHE_SIZE]   |                    | include/linux/slab.h:415          | all, static, external       |
| 16 [ZERO_SIZE_PTR]              |                    | include/linux/slab.h:422          | all, static, external       |
| 1 [GFP_DMA]                     |                    | include/linux/slab.h:418          | all, static, external       |
| 8 [KMALLOC_MIN_SIZE]            |                    | include/linux/slab.h:252          | all, static, external       |
| 64 [KMALLOC_MIN_SIZE]           |                    | include/linux/slab.h:255          | all, static, external       |
| 192 [KMALLOC_MIN_SIZE]          |                    | include/linux/slab.h:257          | all, static, external       |
| 3 [KMALLOC_SHIFT_LOW]           |                    | include/linux/slab.h:253          | all, static, external       |
| 32768 [__GFP_ZERO]              |                    | include/linux/slab.h:578          | all, static, external       |
| 0 [page_to_pfn]                 |                    | include/linux/mm.h:951            | all, static, external       |
| 0 [_THIS_IP_]                   |                    | include/linux/rcupdate.h:418      | all, static, external       |
| 1 [_THIS_IP_]                   |                    | include/linux/rcupdate.h:423      | all, static, external       |
| 4096 [PAGE_SIZE]                |                    | security/tomoyo/common.h:1306     | all, static, external       |
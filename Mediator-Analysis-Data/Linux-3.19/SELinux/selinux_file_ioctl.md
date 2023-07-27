| Source (name [type])            | Field (index [id]) | Source Location                   | Label at Source             |
|---------------------------------|--------------------|-----------------------------------|-----------------------------|
| current                         |                    | security/selinux/hooks.c:3190     | subject, dynamic, input     |
| file                            |                    | security/selinux/hooks.c:3187     | object, dynamic, input      |
| cmd                             |                    | security/selinux/hooks.c:3187     | operation, dynamic, input   |
| 16 [FILE__GETATTR]              |                    | security/selinux/hooks.c:3203     | operation, static, mediator |
| 32 [FILE__SETATTR]              |                    | security/selinux/hooks.c:3209     | operation, static, mediator |
| 0                               |                    | security/selinux/hooks.c:3216     | operation, static, mediator |
| 1 [FILE__IOCTL]                 |                    | security/selinux/hooks.c:3229     | operation, static, mediator |
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
| 0 [_THIS_IP_]                   |                    | include/linux/rcupdate.h:418      | all, static, external       |
| 1 [_THIS_IP_]                   |                    | include/linux/rcupdate.h:423      | all, static, external       |
| -22 [EINVAL]                    |                    | security/selinux/hooks.c:1576     | all, static, external       |
| 1 [SECURITY_CAP_AUDIT]          |                    | security/selinux/hooks.c:1580     | all, static, external       |
| 2097664 [LIST_POISON2]          |                    | include/linux/rculist.h:346       | all, static, external       |
| 2097664 [LIST_POISON2]          |                    | include/linux/rculist.h:366       | all, static, external       |
| 1 [SECURITY_CAP_AUDIT]          |                    | security/selinux/hooks.c:3222     | all, static, external       |
| 1 [FIBMAP]                      |                    | security/selinux/hooks.c:3196     | all, static, external       |
| 21537 [FIONBIO]                 |                    | security/selinux/hooks.c:3213     | all, static, external       |
| 19273 [KDSKBSENT]               |                    | security/selinux/hooks.c:3220     | all, static, external       |
| 19271 [KDSKBENT]                |                    | security/selinux/hooks.c:3219     | all, static, external       |
| 26 [CAP_SYS_TTY_CONFIG]         |                    | security/selinux/hooks.c:3221     | all, static, external       |
| 1074292226 [FS_IOC_SETFLAGS]    |                    | security/selinux/hooks.c:3206     | all, static, external       |
| 1074296322 [FS_IOC_SETVERSION]  |                    | security/selinux/hooks.c:3208     | all, static, external       |
| 21586 [FIOASYNC]                |                    | security/selinux/hooks.c:3215     | all, static, external       |
| 2 [FIGETBSZ]                    |                    | security/selinux/hooks.c:3198     | all, static, external       |
| 21531 [FIONREAD]                |                    | security/selinux/hooks.c:3194     | all, static, external       |
| -2146933247 [FS_IOC_GETFLAGS]   |                    | security/selinux/hooks.c:3200     | all, static, external       |
| -2146929151 [FS_IOC_GETVERSION] |                    | security/selinux/hooks.c:3202     | all, static, external       |

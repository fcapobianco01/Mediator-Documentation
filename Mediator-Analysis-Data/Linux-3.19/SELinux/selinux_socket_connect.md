| Source (name [type])                | Field (index [id]) | Source Location                   | Label at Source             |
|-------------------------------------|--------------------|-----------------------------------|-----------------------------|
| current                             |                    | security/selinux/hooks.c:4137     | subject, dynamic, external  |
| sock                                | 23 [sk_protocol]   | security/selinux/hooks.c:4131     | object, dynamic, input      |
| sock                                | 59 [sk_security]   | security/selinux/hooks.c:4131     | subject, dynamic, input     |
| 2048 [SOCKET__CONNECT]              |                    | security/selinux/hooks.c:4137     | operation, static, mediator |
| 15 [SECCLASS_TCP_SOCKET]            |                    | security/selinux/hooks.c:4169     | all, static, mediator       |
| 44 [SECCLASS_DCCP_SOCKET]           |                    | security/selinux/hooks.c:4145     | all, static, mediator       |
| 67108864 [TCP_SOCKET__NAME_CONNECT] |                    | security/selinux/hooks.c:4170     | all, static, mediator       |
| 8388608 [DCCP_SOCKET__NAME_CONNECT] |                    | security/selinux/hooks.c:4170     | all, static, mediator       |
| 12 [PAGE_SHIFT]                     |                    | include/asm-generic/getorder.h:18 | all, static, external       |
| 64 [BITS_PER_LONG]                  |                    | include/asm-generic/getorder.h:19 | all, static, external       |
| 8192 [KMALLOC_MAX_CACHE_SIZE]       |                    | include/linux/slab.h:415          | all, static, external       |
| 16 [ZERO_SIZE_PTR]                  |                    | include/linux/slab.h:422          | all, static, external       |
| 1 [GFP_DMA]                         |                    | include/linux/slab.h:418          | all, static, external       |
| 8 [KMALLOC_MIN_SIZE]                |                    | include/linux/slab.h:252          | all, static, external       |
| 64 [KMALLOC_MIN_SIZE]               |                    | include/linux/slab.h:255          | all, static, external       |
| 192 [KMALLOC_MIN_SIZE]              |                    | include/linux/slab.h:257          | all, static, external       |
| 3 [KMALLOC_SHIFT_LOW]               |                    | include/linux/slab.h:253          | all, static, external       |
| 32768 [__GFP_ZERO]                  |                    | include/linux/slab.h:578          | all, static, external       |
| 2097664 [LIST_POISON2]              |                    | include/linux/rculist.h:132       | all, static, external       |
| 0 [_THIS_IP_]                       |                    | include/linux/rcupdate.h:418      | all, static, external       |
| 1 [_THIS_IP_]                       |                    | include/linux/rcupdate.h:423      | all, static, external       |
| -22 [EINVAL]                        |                    | security/selinux/hooks.c:4156     | all, static, external       |
| -22 [EINVAL]                        |                    | security/selinux/hooks.c:4161     | all, static, external       |
| 24 [SIN6_LEN_RFC2133]               |                    | include/linux/slab.h:253          | all, static, external       |
| 2 [PF_INET]                         |                    | security/selinux/hooks.c:4153     | all, static, external       |

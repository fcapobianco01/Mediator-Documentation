| Source (name [type])              | Field (index [id]) | Source Location                   | Label at Source             |
| --------------------------------- | ------------------ | --------------------------------- | --------------------------- |
| current                           |                    | security/selinux/hooks.c:4038     | subject, dynamic, external  |
| sock                              | 23 [sk_protocol]   | security/selinux/hooks.c:4032     | object, dynamic, input      |
| sock                              | 59 [sk_security]   | security/selinux/hooks.c:4032     | subject, dynamic, input     |
| 1024 [SOCKET__BIND]               |                    | security/selinux/hooks.c:4038     | operation, static, mediator |
| 2097152 [SOCKET__NAME_BIND]       |                    | security/selinux/hooks.c:4084     | operation, static, mediator |
| 15 [SECCLASS_TCP_SOCKET]          |                    | security/selinux/hooks.c:4091     | all, static, mediator       |
| 16 [SECCLASS_UDP_SOCKET]          |                    | security/selinux/hooks.c:4095     | all, static, mediator       |
| 44 [SECCLASS_DCCP_SOCKET]         |                    | security/selinux/hooks.c:4099     | all, static, mediator       |
| 33554432 [TCP_SOCKET__NODE_BIND]  |                    | security/selinux/hooks.c:4092     | all, static, mediator       |
| 4194304 [UDP_SOCKET__NODE_BIND]   |                    | security/selinux/hooks.c:4096     | all, static, mediator       |
| 4194304 [DCCP_SOCKET__NODE_BIND]  |                    | security/selinux/hooks.c:4100     | all, static, mediator       |
| 4194304 [RAWIP_SOCKET__NODE_BIND] |                    | security/selinux/hooks.c:4104     | all, static, mediator       |
| 12 [PAGE_SHIFT]                   |                    | include/asm-generic/getorder.h:18 | all, static, external       |
| 64 [BITS_PER_LONG]                |                    | include/asm-generic/getorder.h:19 | all, static, external       |
| 8192 [KMALLOC_MAX_CACHE_SIZE]     |                    | include/linux/slab.h:415          | all, static, external       |
| 16 [ZERO_SIZE_PTR]                |                    | include/linux/slab.h:422          | all, static, external       |
| 1 [GFP_DMA]                       |                    | include/linux/slab.h:418          | all, static, external       |
| 8 [KMALLOC_MIN_SIZE]              |                    | include/linux/slab.h:252          | all, static, external       |
| 64 [KMALLOC_MIN_SIZE]             |                    | include/linux/slab.h:255          | all, static, external       |
| 192 [KMALLOC_MIN_SIZE]            |                    | include/linux/slab.h:257          | all, static, external       |
| 3 [KMALLOC_SHIFT_LOW]             |                    | include/linux/slab.h:253          | all, static, external       |
| 32768 [__GFP_ZERO]                |                    | include/linux/slab.h:578          | all, static, external       |
| 2097664 [LIST_POISON2]            |                    | include/linux/rculist.h:132       | all, static, external       |
| 0 [_THIS_IP_]                     |                    | include/linux/rcupdate.h:418      | all, static, external       |
| 1 [_THIS_IP_]                     |                    | include/linux/rcupdate.h:423      | all, static, external       |
| 2 [PF_INET]                       |                    | include/linux/rcupdate.h:423      | all, static, external       |
| 2 [PF_INET]                       |                    | include/linux/rcupdate.h:423      | all, static, external       |
| 2 [PF_INET]                       |                    | include/linux/rcupdate.h:423      | all, static, external       |
| 1024 [PROT_SOCK]                  |                    | include/linux/rcupdate.h:423      | all, static, external       |
| 10 [PF_INET6]                     |                    | include/linux/rcupdate.h:423      | all, static, external       |
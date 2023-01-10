| Source (name [type])                          | Field (index [id]) | Source Location                    | Label at Source             |
|-----------------------------------------------|--------------------|------------------------------------|-----------------------------|
| current                                       |                    | security/selinux/hooks.c:3982      | subject, dynamic, external  |
| tsec                                          | 1 [sid]            | security/selinux/hooks.c:3982      | subject, dynamic, input     |
| tsec                                          | 5 [sockcreate_sid] | security/selinux/hooks.c:3982      | object, dynamic, input      |
| 8 [SOCKET__CREATE]                            |                    | security/selinux/hooks.c:3995      | operation, static, mediator |
| 23 [SECCLASS_UNIX_STREAM_SOCKET]              |                    | security/selinux/hooks.c:1177      | all, static, mediator       |
| 24 [SECCLASS_UNIX_DGRAM_SOCKET]               |                    | security/selinux/hooks.c:1179      | all, static, mediator       |
| 15 [SECCLASS_TCP_SOCKET]                      |                    | security/selinux/hooks.c:1187      | all, static, mediator       |
| 17 [SECCLASS_RAWIP_SOCKET]                    |                    | security/selinux/hooks.c:1189      | all, static, mediator       |
| 16 [SECCLASS_UDP_SOCKET]                      |                    | security/selinux/hooks.c:1192      | all, static, mediator       |
| 17 [SECCLASS_RAWIP_SOCKET]                    |                    | security/selinux/hooks.c:1194      | all, static, mediator       |
| 44 [SECCLASS_DCCP_SOCKET]                     |                    | security/selinux/hooks.c:1196      | all, static, mediator       |
| 17 [SECCLASS_RAWIP_SOCKET]                    |                    | security/selinux/hooks.c:1198      | all, static, mediator       |
| 30 [SECCLASS_NETLINK_ROUTE_SOCKET]            |                    | security/selinux/hooks.c:1204      | all, static, mediator       |
| 31 [SECCLASS_NETLINK_FIREWALL_SOCKET]         |                    | security/selinux/hooks.c:1206      | all, static, mediator       |
| 32 [SECCLASS_NETLINK_TCPDIAG_SOCKET]          |                    | security/selinux/hooks.c:1208      | all, static, mediator       |
| 33 [SECCLASS_NETLINK_NFLOG_SOCKET]            |                    | security/selinux/hooks.c:1210      | all, static, mediator       |
| 34 [SECCLASS_NETLINK_XFRM_SOCKET]             |                    | security/selinux/hooks.c:1212      | all, static, mediator       |
| 35 [SECCLASS_NETLINK_SELINUX_SOCKET]          |                    | security/selinux/hooks.c:1214      | all, static, mediator       |
| 36 [SECCLASS_NETLINK_AUDIT_SOCKET]            |                    | security/selinux/hooks.c:1216      | all, static, mediator       |
| 37 [SECCLASS_NETLINK_IP6FW_SOCKET]            |                    | security/selinux/hooks.c:1218      | all, static, mediator       |
| 38 [SECCLASS_NETLINK_DNRT_SOCKET]             |                    | security/selinux/hooks.c:1220      | all, static, mediator       |
| 40 [SECCLASS_NETLINK_KOBJECT_UEVENT_SOCKET]   |                    | security/selinux/hooks.c:1222      | all, static, mediator       |
| 20 [SECCLASS_NETLINK_SOCKET]                  |                    | security/selinux/hooks.c:1224      | all, static, mediator       |
| 21 [SECCLASS_PACKET_SOCKET]                   |                    | security/selinux/hooks.c:1227      | all, static, mediator       |
| 22 [SECCLASS_KEY_SOCKET]                      |                    | security/selinux/hooks.c:1229      | all, static, mediator       |
| 41 [SECCLASS_APPLETALK_SOCKET]                |                    | security/selinux/hooks.c:1231      | all, static, mediator       |
| 14 [SECCLASS_SOCKET]                          |                    | security/selinux/hooks.c:1234      | all, static, mediator       |
| 12 [PAGE_SHIFT]                               |                    | include/asm-generic/getorder.h:18  | all, static, external       |
| 64 [BITS_PER_LONG]                            |                    | include/asm-generic/getorder.h:19  | all, static, external       |
| 8192 [KMALLOC_MAX_CACHE_SIZE]                 |                    | include/linux/slab.h:415           | all, static, external       |
| 16 [ZERO_SIZE_PTR]                            |                    | include/linux/slab.h:422           | all, static, external       |
| 1 [GFP_DMA]                                   |                    | include/linux/slab.h:418           | all, static, external       |
| 8 [KMALLOC_MIN_SIZE]                          |                    | include/linux/slab.h:252           | all, static, external       |
| 64 [KMALLOC_MIN_SIZE]                         |                    | include/linux/slab.h:255           | all, static, external       |
| 192 [KMALLOC_MIN_SIZE]                        |                    | include/linux/slab.h:257           | all, static, external       |
| 3 [KMALLOC_SHIFT_LOW]                         |                    | include/linux/slab.h:253           | all, static, external       |
| 32768 [__GFP_ZERO]                            |                    | include/linux/slab.h:578           | all, static, external       |
| 17 [IPPROTO_UDP]                              |                    | security/selinux/hooks.c:1167      | all, static, external       |
| 0 [IPPROTO_IP]                                |                    | security/selinux/hooks.c:1167      | all, static, external       |
| 6 [IPPROTO_TCP]                               |                    | security/selinux/hooks.c:1162      | all, static, external       |
| 0 [IPPROTO_IP]                                |                    | security/selinux/hooks.c:1162      | all, static, external       |
| 3 [NETLINK_FIREWALL]                          |                    | security/selinux/hooks.c:1205      | all, static, external       |
| 16 [PF_NETLINK]                               |                    | security/selinux/hooks.c:1201      | all, static, external       |
| 4 [NETLINK_SOCK_DIAG]                         |                    | security/selinux/hooks.c:1207      | all, static, external       |
| 7 [NETLINK_SELINUX]                           |                    | security/selinux/hooks.c:1213      | all, static, external       |
| 13 [NETLINK_IP6_FW]                           |                    | security/selinux/hooks.c:1217      | all, static, external       |
| 5 [NETLINK_NFLOG]                             |                    | security/selinux/hooks.c:1209      | all, static, external       |
| 14 [NETLINK_DNRTMSG]                          |                    | security/selinux/hooks.c:1219      | all, static, external       |
| 15 [PF_KEY]                                   |                    | security/selinux/hooks.c:1228      | all, static, external       |
| 2 [PF_INET]                                   |                    | security/selinux/hooks.c:1182      | all, static, external       |
| 9 [NETLINK_AUDIT]                             |                    | security/selinux/hooks.c:1215      | all, static, external       |
| 0 [NETLINK_ROUTE]                             |                    | security/selinux/hooks.c:1203      | all, static, external       |
| 6 [NETLINK_XFRM]                              |                    | security/selinux/hooks.c:1211      | all, static, external       |
| 5 [PF_APPLETALK]                              |                    | security/selinux/hooks.c:1230      | all, static, external       |
| 10 [PF_INET6]                                 |                    | security/selinux/hooks.c:1183      | all, static, external       |
| 17 [PF_PACKET]                                |                    | security/selinux/hooks.c:1226      | all, static, external       |
| 15 [NETLINK_KOBJECT_UEVENT]                   |                    | security/selinux/hooks.c:1221      | all, static, external       |
| 1 [PF_UNIX]                                   |                    | security/selinux/hooks.c:1173      | all, static, external       |


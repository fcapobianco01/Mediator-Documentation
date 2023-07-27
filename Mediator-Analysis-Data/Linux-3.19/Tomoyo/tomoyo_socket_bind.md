| Source                     | Field Index | Location                      | Label at Source             |
|----------------------------|-------------|-------------------------------|-----------------------------|
| 0 [TOMOYO_NETWORK_BIND]    |             | security/tomoyo/network.c:732 | operation, static, mediator |
| sock                       |             | security/tomoyo/tomoyo.c:481  | object, dynamic, input      |
| addr_len                   |             | security/tomoyo/tomoyo.c:481  | object, dynamic, input      |
| addr                       |             | security/tomoyo/tomoyo.c:481  | object, dynamic, input      |
| 2 [SOCK_STREAM]            |             | security/tomoyo/network.c:727 | all, static, external       |
| 1 [SOCK_DGRAM]             |             | security/tomoyo/network.c:728 | all, static, external       |
| 3 [SOCK_RAW]               |             | security/tomoyo/network.c:729 | all, static, external       |
| 5 [SOCK_SEQPACKET]         |             | security/tomoyo/network.c:730 | all, static, external       |
| 2 [PF_INET]                |             | security/tomoyo/network.c:629 | all, static, external       |
| 10 [PF_INET6]              |             | security/tomoyo/network.c:630 | all, static, external       |
| 1 [PF_UNIX]                |             | security/tomoyo/network.c:737 | all, static, external       |
| 24 [SIN6_LEN_RFC2133]      |             | security/tomoyo/network.c:509 | all, static, external       |
| 10 [AF_INET6]              |             | security/tomoyo/network.c:508 | all, static, external       |
| 2 [AF_INET]                |             | security/tomoyo/network.c:516 | all, static, external       |
| 0 [TOMOYO_CONFIG_DISABLED] |             | security/tomoyo/network.c:549 | all, static, mediator       |
| 0 [TOMOYO_CONFIG_DISABLED] |             | security/tomoyo/network.c:474 | all, static, mediator       |
| "anonymous"                |             | security/tomoyo/network.c:554 | all, static, mediator       |
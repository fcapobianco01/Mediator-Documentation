| Source                     | Field Index | Location                      | Label at Source             |
|----------------------------|-------------|-------------------------------|-----------------------------|
| 1 [TOMOYO_NETWORK_LISTEN]  |             | security/tomoyo/network.c:663 | operation, static, mediator |
| sock                       |             | security/tomoyo/tomoyo.c:452  | object, dynamic, input      |
| 2 [SOCK_STREAM]            |             | security/tomoyo/network.c:653 | all, static, external       |
| 5 [SOCK_SEQPACKET]         |             | security/tomoyo/network.c:653 | all, static, external       |
| 1 [PF_UNIX]                |             | security/tomoyo/network.c:737 | all, static, external       |
| 2 [PF_INET]                |             | security/tomoyo/network.c:629 | all, static, external       |
| 10 [PF_INET6]              |             | security/tomoyo/network.c:630 | all, static, external       |
| 24 [SIN6_LEN_RFC2133]      |             | security/tomoyo/network.c:509 | all, static, external       |
| 10 [AF_INET6]              |             | security/tomoyo/network.c:508 | all, static, external       |
| 2 [AF_INET]                |             | security/tomoyo/network.c:516 | all, static, external       |
| 0 [TOMOYO_CONFIG_DISABLED] |             | security/tomoyo/network.c:549 | all, static, mediator       |
| 0 [TOMOYO_CONFIG_DISABLED] |             | security/tomoyo/network.c:474 | all, static, mediator       |
| "anonymous"                |             | security/tomoyo/network.c:554 | all, static, mediator       |
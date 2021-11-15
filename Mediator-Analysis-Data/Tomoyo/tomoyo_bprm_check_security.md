| Source (name [type]) | Field (index [id]) | Source Location | Label at Source |
| ------ | ----------- | -------- | --------------- | ---------------- | --------------- | ------- |
| bprm [linux_binprm] |  | security/tomoyo/tomoyo.c: 118	| operation, dynamic, input |
| domain [tomoyo_domain_info] | security/tomoyo/tomoyo.c: 120 | subject, dynamic, input |
| 1 [TOMOYO_TYPE_READ] | | security/tomoyo/file.c: 759	| operation, static, mediator |
| 2 [TOMOYO_TYPE_APPEND] | | security/tomoyo/file.c: 762 | operation, static, mediator |
| 3 [TOMOYO_TYPE_WRITE] | | security/tomoyo/file.c: 762	| operation, static, mediator |
| buf [tomoyo_path_info] | 0 [name] | security/tomoyo/file.c: 747 | object, dynamic, mediator |
| f [file] | 1 [f_path] | security/tomoyo/tomoyo.c: 329 | object, dynamic, input |
| current | | security/tomoyo/tomoyo.c: 18 | subject, dynamic, external |
| task_security_struct | | security/tomoyo/tomoyo.c: 18 | subject, dynamic, external |
| 0 [TOMOYO_TYPE_PATH_ACL] | | security/tomoyo/file.c: 567 | policy, static, mediator |
| r [tomoyo_request_info] | 2 [domain] | security/tomoyo/util.c: 1022 | subject, dynamic, external |
| r [tomoyo_request_info] | 3->0 [param.path.filename] | security/tomoyo/file.c: 568 | object, dynamic, external |
| r [tomoyo_request_info] | 3->2 [param.path.operation] | security/tomoyo/file.c: 569 | operation, dynamic, external |
| r [tomoyo_request_info] | 6 [param_type] | security/tomoyo/file.c: 567 | policy, static, mediator |
| 0 [TOMOYO_CONFIG_DISABLED] | | security/tomoyo/file.c: 748 | static, mediator |
| 3 [TOMOYO_CONFIG_ENFORCING] | | security/tomoyo/file.c: 770 | static, mediator |
| 2 [MAY_WRITE] | | include/linux/fs.h: 73 | static, external |
| 4 [MAY_READ] | | include/linux/fs.h: 74 | static, external |
| 1 [TOMOYO_MAC_FILE_OPEN] | | security/tomoyo/file.c: 751 | static, mediator |
| '\0' | | security/tomoyo/realpath.c: 269 | static, mediator |
| 256 | | security/tomoyo/realpath.c: 125 | static, mediator |
| '/' | | security/tomoyo/realpath.c: 158 | static, mediator |
| '/' | | security/tomoyo/realpath.c: 127 | static, mediator |
| '/' | | security/tomoyo/realpath.c: 130 | static, mediator |
| "dev(%u,%u):"	| |	security/tomoyo/realpath.c: 185 | static, mediator |
| ':' | | security/tomoyo/realpath.c: 203 | static, mediator |
| 2048 [PAGE_SIZE] | | arch/x86/include/asm/page_types.h: 9	| static, external |
| 80 | | include/linux/gfp.h: 108 | static, external |

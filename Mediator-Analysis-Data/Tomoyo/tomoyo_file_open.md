| Source (name [type]) | Field (index [id]) | Source Location | Label at Source | Label Gap @ Sink | Endorser @ Sink | Remarks |
| ------ | ----------- | -------- | --------------- | ---------------- | --------------- | ------- |
| f [file] | 6 [f_flags] | security/tomoyo/tomoyo.c: 329	| operation, dynamic, input | value | | The next 3 rows of constants serves as the operation used by tomoyo_request_info, but takes an implicit flow from this row. Since the mapping from f->f_flags to the 3 constants is not a trivial 1-to-1 mapping, an ad hoc endorser seems to be necessary here. |
| 1 [TOMOYO_TYPE_READ] | | security/tomoyo/file.c: 759	| operation, static, mediator | purpose, value | E3 | See above |
| 2 [TOMOYO_TYPE_APPEND] | | security/tomoyo/file.c: 762 | operation, static, mediator | purpose, value | E3 | See above |
| 3 [TOMOYO_TYPE_WRITE] | | security/tomoyo/file.c: 762	| operation, static, mediator | purpose, value | E3 | See above |
| buf [tomoyo_path_info] | 0 [name] | security/tomoyo/file.c: 747 | object, dynamic, mediator | | | Intermediate object |
| f [file] | 1 [f_path] | security/tomoyo/tomoyo.c: 329 | object, dynamic, input | purpose, source | E4 | Source for object |
| current | | security/tomoyo/tomoyo.c: 18 | subject, dynamic, external | source | E4 | |
| task_security_struct | | security/tomoyo/tomoyo.c: 18 | subject, dynamic, external | | | |
| 0 [TOMOYO_TYPE_PATH_ACL] | | security/tomoyo/file.c: 567 | policy, static, mediator | purpose, value | E3 | Source for policy |
| r [tomoyo_request_info] | 2 [domain] | security/tomoyo/util.c: 1022 | subject, dynamic, external | source | E4 | Sink for subject | 
| r [tomoyo_request_info] | 3->0 [param.path.filename] | security/tomoyo/file.c: 568 | object, dynamic, external | source | E4 | Union holding both the object and operation. Since information flow analysis can differentiate fields in the union, the gap in purpose dimension is eliminated |
| r [tomoyo_request_info] | 3->2 [param.path.operation] | security/tomoyo/file.c: 569 | operation, dynamic, external | value | E3 | Union holding both the object and operation. Since information flow analysis can differentiate fields in the union, the gap in purpose dimension is eliminated |
| r [tomoyo_request_info] | 6 [param_type] | security/tomoyo/file.c: 567 | policy, static, mediator | purpose, value | E3 | Sink for policy |
| 0 [TOMOYO_CONFIG_DISABLED] | | security/tomoyo/file.c: 748 | static, mediator | | | |
| 3 [TOMOYO_CONFIG_ENFORCING] | | security/tomoyo/file.c: 770 | static, mediator | | | |
| 2 [MAY_WRITE] | | include/linux/fs.h: 73 | static, external | | | Implicity source for opereation |
| 4 [MAY_READ] | | include/linux/fs.h: 74 | static, external | | | Implicity source for opereation |
| 1 [TOMOYO_MAC_FILE_OPEN] | | security/tomoyo/file.c: 751 | static, mediator | | | |
| '\0' | | security/tomoyo/realpath.c: 269 | static, mediator | | | Null terminator |
| 256 | | security/tomoyo/realpath.c: 125 | static, mediator | | | |
| '/' | | security/tomoyo/realpath.c: 158 | static, mediator | | | |
| '/' | | security/tomoyo/realpath.c: 127 | static, mediator | | | |
| '/' | | security/tomoyo/realpath.c: 130 | static, mediator | | | |
| "dev(%u,%u):"	| |	security/tomoyo/realpath.c: 185 | static, mediator | | | |
| ':' | | security/tomoyo/realpath.c: 203 | static, mediator | | | |
| 2048 [PAGE_SIZE] | | arch/x86/include/asm/page_types.h: 9	| static, external | | | Used in kmalloc for path buffer. Seems to be 4096, not 2048.  |
| 80 | | include/linux/gfp.h: 108 | static, external | | | Used in kmalloc for path buffer |
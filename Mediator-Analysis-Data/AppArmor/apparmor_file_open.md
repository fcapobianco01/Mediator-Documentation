| Source (name [type]) | Field (index [id]) | Source Location | Label at Source |
| -------------------- | ------------------ | --------------- | --------------- |
| file [file] | 1 | security/apparmor/lsm.c:376 | object, dynamic, input |
| cred [cred] |  | security/apparmor/lsm.c:376 | subject, dynamic, input |
| profile [aa_profile] |  | security/apparmor/lsm.c:379 | subject, dynamic, external |
| 2 [FMODE_WRITE] |  | include/linux/fs.h:90 | operation, static, external |
| 2 [MAY_WRITE] | | include/linux/fs.h:73  | operation, static, external |
| 1 [FMODE_READ] |  | include/linux/fs.h:88 | operation, static, external |
| 4 [MAY_READ] |  | include/linux/fs.h:74 | operation, static, external |
| 16 [AA_MAY_CREATE] |  | security/apparmor/include/file.h:28 | operation, static, mediator |
| 64 [O_CREAT] |  | include/uapi/asm-generic/fcntl.h:23 | operation, static, external |
| 512 [O_TRUNC] |  | include/uapi/asm-generic/fcntl.h:32 | operation, static, external |
| 1024 [O_APPEND] |  | include/uapi/asm-generic/fcntl.h:35 | operation, static, external |
| 8 [MAY_APPEND] | | include/linux/fs.h:75  | operation, static, external |
| -3 [~MAY_WRITE] |  | security/apparmor/include/file.h:206 | operation, static, mediator |
| 1 [MAY_EXEC] |  | include/linux/fs.h:72 | operation, static, external |
| 2053 [AA_EXEC_MMAP] |  | /security/apparmor/include/file.h:36 | operation, static, mediator |
| file [file] | 14 | security/apparmor/lsm.c:378 | object, dynamic, input |
| inode [file] | 2 | /security/apparmor/lsm.c:397 | object, dynamic, input |
| 18 [OP_OPEN] |  | /include/linux/nfs4.h:69 | operation, static, external |

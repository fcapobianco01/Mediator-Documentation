| Source (name [type]) | Field (index [id]) | Source Location | Label at Source |
| -------------------- | ------------------ | --------------- | --------------- |
| dir [inode] |  | security/selinux/hooks.c:2777 | object, dynamic, input |
| dentry [dentry] |  | security/selinux/hooks.c:2777 | object, dynamic, input |
| tsec [task_security_struct] |  | security/selinux/hooks.c:1706 | subject, dynamic, input |
| dsec [inode_security_struct] |  | security/selinux/hooks.c:1707 | object, dynamic, input |
| 7 [SECCLASS_DIR] |  | security/selinux/hooks.c:1722 | operation, static, mediator |
| 9437184 [DIR__ADD_NAME bitwise-or DIR__SEARCH] |  | security/selinux/hooks.c:1722 | operation, static, mediator |
| 5 [SECCLASS_FILESYSTEM] |  | /security/selinux/hooks.c:1739 | operation, static, mediator |
| 128 [FILESYSTEM__ASSOCIATE] |  | /security/selinux/hooks.c:1739 | operation, static, mediator |
| 8 [FILE__CREATE] |  | /security/selinux/hooks.c:1735 | operation, static, mediator |
| 49152 [SECCLASS_SOCK_FILE] |  | /security/selinux/hooks.c:1141 | operation, static, mediator |
| 40960 [SECCLASS_LNK_FILE] |  | /security/selinux/hooks.c:1143 | operation, static, mediator |
| 32768 [SECCLASS_FILE] |  | /security/selinux/hooks.c:1145 | operation, static, mediator |
| 24576 [SECCLASS_BLK_FILE] |  | /security/selinux/hooks.c:1147 | operation, static, mediator |
| 16384 [SECCLASS_DIR] |  | /security/selinux/hooks.c:1149 | operation, static, mediator |
| 8192 [SECCLASS_CHR_FILE] |  | /security/selinux/hooks.c:1151 | operation, static, mediator |
| 4096 [SECCLASS_FIFO_FILE] |  | /security/selinux/hooks.c:1153 | operation, static, mediator |

| Source (name [type]) | Field (index [id]) | Source Location | Label at Source |
| -------------------- | ------------------ | --------------- | --------------- |
| dir [inode] |  | security/selinux/hooks.c:2777 | object, dynamic, input |
| dentry [dentry] |  | security/selinux/hooks.c:2777 | object, dynamic, input |
| 9 [SECCLASS_LNK_FILE] |  | security/selinux/hooks.c:2779 | operation, static, mediator |
| tsec [task_security_struct] |  | security/selinux/hooks.c:1706 | subject, dynamic, input |
| dsec [inode_security_struct] |  | security/selinux/hooks.c:1707 | object, dynamic, input |
| 7 [SECCLASS_DIR] |  | security/selinux/hooks.c:1722 | operation, static, mediator |
| 9437184 [DIR__ADD_NAME ^ DIR__SEARCH] |  | security/selinux/hooks.c:1722 | operation, static, mediator |
| 5 [SECCLASS_FILESYSTEM] |  | /security/selinux/hooks.c:1739 | operation, static, mediator |
| 128 [FILESYSTEM__ASSOCIATE] |  | /security/selinux/hooks.c:1739 | operation, static, mediator |
| 8 [FILE__CREATE] |  | /security/selinux/hooks.c:1735 | operation, static, mediator |
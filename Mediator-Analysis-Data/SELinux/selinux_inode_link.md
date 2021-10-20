| Source (name [type]) | Field (index [id]) | Source Location | Label at Source |
| -------------------- | ------------------ | --------------- | --------------- |
| dir [inode] |  | security/selinux/hooks.c:2777 | object, dynamic, input |
| dentry [dentry] |  | security/selinux/hooks.c:2777 | object, dynamic, input |
| 0 [MAY_LINK] |  | security/selinux/hooks.c:2777 | operation, static, mediator |
| tsec [task_security_struct] |  | security/selinux/hooks.c:218 | subject, dynamic, input |
| dsec [inode_security_struct] |  | security/selinux/hooks.c:1769 | object, dynamic, input |
| isec [inode_security_struct] |  | security/selinux/hooks.c:1770 | object, dynamic, input |
| 7 [SECCLASS_DIR] |  | security/selinux/hooks.c:1722 | operation, static, mediator |
| 0 [FILE__LINK] |  | security/selinux/hooks.c:1783 | operation, static, mediator |
| 1 [FILE__UNLINK] |  | security/selinux/hooks.c:1783 |  operation, static, mediator|
| 2 [DIR__RMDIR] |  | security/selinux/hooks.c:1783 | operation, static, mediator |
| 8388608 [DIR__SEARCH] |  | security/selinux/hooks.c:1775 | operation, static, mediator |
| 2097152 [DIR__REMOVE_NAME] |  | security/selinux/hooks.c:1776 | operation, static, mediator |
| 1048576 [DIR__ADD_NAME] |  | security/selinux/hooks.c:1776 | operation, static, mediator |
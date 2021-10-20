| Source (name [type]) | Field (index [id]) | Source Location | Label at Source |
| -------------------- | ------------------ | --------------- | --------------- |
| old_inode [inode] |  | security/selinux/hooks.c:2797 | object, dynamic, input |
| new_inode [inode] |  | security/selinux/hooks.c:2797 | object, dynamic, input |
| old_dentry [dentry] |  | security/selinux/hooks.c:2797 | object, dynamic, input |
| new_dentry [dentry] |  | security/selinux/hooks.c:2797 | object, dynamic, input |
| old_dsec [inode_security_struct] |  | security/selinux/hooks.c:1813| object, dynamic, input |
| new_dsec [inode_security_struct] |  | security/selinux/hooks.c:1816 | object, dynamic, input |
| old_isec [inode_security_struct] |  | security/selinux/hooks.c:1814 | object, dynamic, input |
| new_isec [inode_security_struct] |  | security/selinux/hooks.c:1844 | object, dynamic, input |
| tsec [task_security_struct] |  | security/selinux/hooks.c:218 | subject, dynamic, input |
| 7 [SECCLASS_DIR] |  | security/selinux/hooks.c:1821 | operation, static, mediator |
| 10485760 [DIR__REMOVE_NAME bitwise-or DIR__SEARCH] |  | security/selinux/hooks.c:1821 | operation, static, mediator |
| 4096 [FILE__RENAME] |  | security/selinux/hooks.c:1825 | operation, static, mediator |
| 4194304 [DIR_REPARENT] |  | security/selinux/hooks.c:1830 | operation, static, mediator |
| 1024 [FILE__UNLINK] |  | security/selinux/hooks.c:1846 | operation, static, mediator |
| 16777216 [DIR__RMDIR] |  | security/selinux/hooks.c:1846 | operation, static, mediator |
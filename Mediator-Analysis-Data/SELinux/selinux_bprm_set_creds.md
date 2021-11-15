| Source (name [type]) | Field (index [id]) | Source Location | Label at Source |
| -------------------- | ------------------ | --------------- | --------------- |
| bprm [linux_binprm] |  | security/selinux/hooks.c:2133 | object, dynamic, input |
| old_tsec [task_security_struct] | | security/selinux/hooks.c: 2135 | subject, dynamic, external |
| new_tsec [task_security_struct] | | security/selinux/hooks.c: 2136 | object, dynamic, input |
| isec [inode_security_struct] | | security/selinux/hooks.c: 2137 | object, dynamic, input |
| type [typew_datum] | | security/selinux/ss/services.c: 822 | dynamic, mediator |
| policydb | | security/selinux/ss/services.c: 851 | policy, dynamic, external |
| 2 [FILE__EXECUTE_NO_TRANS] |  | /security/selinux/include/av_permissions.h:92 | operation, static, mediator |
| 2097152 [PROCESS_TRANSITION] |  | /security/selinux/include/av_permissions.h:85 | operation, static, mediator |
| 32768 [FILE_ENTRYPOINT] |  | /security/selinux/include/av_permissions.h:83 | operation, static, mediator |
| 128 [PROCESS_SHARE] |  | /security/selinux/include/av_permissions.h:83 | operation, static, mediator |
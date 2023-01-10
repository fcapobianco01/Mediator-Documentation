| Source (name [type])   | Field (index [id]) | Source Location               | Label at Source             |
|------------------------|--------------------|-------------------------------|-----------------------------|
| current                |                    | security/selinux/hooks.c:2880 | subject, dynamic, external  |
| dentry                 |                    | security/selinux/hooks.c:2878 | object, dynamic, input      |
| 4 [FILE__WRITE]        |                    | security/selinux/hooks.c:2882 | operation, static, mediator |
| 32 [FILE__SETATTR]     |                    | security/selinux/hooks.c:2882 | operation, static, mediator |
| 262144 [FILE__OPEN]    |                    | security/selinux/hooks.c:2882 | operation, static, mediator |
| 512 [ATTR_FORCE]       |                    | security/selinux/hooks.c:2885 | all, static, external       |
| 512 [ATTR_FORCE]       |                    | security/selinux/hooks.c:2887 | all, static, external       |
| 8 [ATTR_SIZE]          |                    | security/selinux/hooks.c:2896 | all, static, external       |
| 1 [ATTR_MODE]          |                    | security/selinux/hooks.c:2886 | all, static, external       |
| 1 [ATTR_MODE]          |                    | security/selinux/hooks.c:2892 | all, static, external       |
| 256 [ATTR_MTIME_SET]   |                    | security/selinux/hooks.c:2893 | all, static, external       |
| 4096 [ATTR_KILL_SGID]  |                    | security/selinux/hooks.c:2886 | all, static, external       |
| 4 [ATTR_GID]           |                    | security/selinux/hooks.c:2892 | all, static, external       |
| 65536 [ATTR_TIMES_SET] |                    | security/selinux/hooks.c:2893 | all, static, external       |
| 2 [ATTR_UID]           |                    | security/selinux/hooks.c:2892 | all, static, external       |
| 2048 [ATTR_KILL_SUID]  |                    | security/selinux/hooks.c:2886 | all, static, external       |
| 128 [ATTR_ATIME_SET]   |                    | security/selinux/hooks.c:2893 | all, static, external       |
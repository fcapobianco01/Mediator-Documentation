| Source (name [type])                    | Field (index [id]) | Source Location               | Label at Source            |
|-----------------------------------------|--------------------|-------------------------------|----------------------------|
| current                                 |                    | security/selinux/hooks.c:2915 | subject, dynamic, external |
| dentry                                  |                    | security/selinux/hooks.c:3053 | object, dynamic, input     |
| "selinux" [XATTR_SELINUX_SUFFIX]        |                    | security/selinux/hooks.c:3055 | all, static, external      |
| "security." [XATTR_SECURITY_PREFIX]     |                    | security/selinux/hooks.c:2917 | all, static, external      |
| "security." [XATTR_SECURITY_PREFIX]     |                    | security/selinux/hooks.c:2918 | all, static, external      |
| "security.capability" [XATTR_NAME_CAPS] |                    | security/selinux/hooks.c:2918 | all, static, external      |
| -13 [EACCES]                            |                    | security/selinux/hooks.c:3060 | all, static, external      |
| 31 [CAP_SETFCAP]                        |                    | security/selinux/hooks.c:2920 | all, static, external      |
| 21 [CAP_SYS_ADMIN]                      |                    | security/selinux/hooks.c:2922 | all, static, external      |
| -1 [EPERM]                              |                    | security/selinux/hooks.c:2921 | all, static, external      |
| -1 [EPERM]                              |                    | security/selinux/hooks.c:2925 | all, static, external      |
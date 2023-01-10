| Source (name [type])  | Field (index [id]) | Source Location               | Label at Source             |
|-----------------------|--------------------|-------------------------------|-----------------------------|
| current               |                    | security/selinux/hooks.c:218  | subject, dynamic, external  |
| shp                   |                    | security/selinux/hooks.c:5369 | object, dynamic, input      |
| 16 [SHM__READ]        |                    | security/selinux/hooks.c:5375 | operation, static, mediator |
| 32 [SHM__WRITE]       |                    | security/selinux/hooks.c:5377 | operation, static, mediator |
| 16 [SHM__READ]        |                    | security/selinux/hooks.c:5377 | operation, static, mediator |
| 4096 [SHM_RDONLY]     |                    | security/selinux/hooks.c:5374 | all, static, external       |
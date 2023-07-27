| Source (name [type]) | Field (index [id]) | Source Location                          | Label at Source             |
|----------------------|--------------------|------------------------------------------|-----------------------------|
| file                 |                    | security/apparmor/lsm.c:454              | object, dynamic, input      |
| mask                 |                    | security/apparmor/lsm.c:454              | operation, dynamic, input   |
| 17 [OP_FPERM]        |                    | security/apparmor/lsm.c:456              | operation, static, mediator |
| 0 [MS_NOUSER]        |                    | security/apparmor/include/apparmor.h:117 | all, static, external       |
| current              |                    | security/apparmor/include/context.h:99   | subject, dynamic, external  |
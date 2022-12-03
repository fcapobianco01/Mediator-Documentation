We record here a series of hook function which returns success in special scenarios.

### SELinux

#### `selinux_sem_semctl`, `selinux_shm_shmctl`, `selinux_msg_queue_msgctl`, 
Returning 0 when `cmd` is not in the set of expected values.

#### Lines removed with relaxed noninterference update
```
1611
1683
1694
3350
```
189 total relaxed annotations for previous version.
117 for tomoyo, reduced to 31.
#### **


`selinux_syslog` Should this one be annotated? current are the same, but appear at different places.

`selinux_inode_link` This is a FP because of the implicit assignment in IR at 1797

`file_map_prot_check` Visit this function.

`selinux_file_mprotect` 3328 questionable.

`selinux_quotactl` 2036, explicitly states */\* let the kernel handle invalid cmds \*/*

`selinux_netlink_send` always return 0 on 5069

`selinux_sb_kern_mount` 2614, */\* Allow all mounts performed by the kernel \*/*

`selinux_task_setrlimit` return explicit 0 when the old_limit equals new_limit on their max value.

`apparmor_file_lock` lsm.c:463, in theory, this branch should not be relaxed, but...

`may_create`

questionable `selinux` lines/hooks: 1565, 5519, 1728, 1731, 2885, 4724, `selinux_inode_setxattr`, `selinux_socket_bind`(4068, 4073)



### old relaxed - new relaxed

### SELinux

confirmed - `selinux_secmark_enabled(), selinux_authorizable_xfrm(x), IS_PRIVATE(inode)`, family of `capable`
```
1611
3253
3165
5519
2852
5783
```

questionable
```
1683
1694
3169
4724
4374
4401
3628
```

should be removed without question
```
1565
3350
1902
1904
1905
1945
1874
5488
5490
4058
4068
4073
4048
```


### Tomoyo

confirmed - `tomoyo_init_request_info`
```
750
565
797
898
899

```

questionable
```
315 - tomoyo.c
379 - tomoyo.c
382 - tomoyo.c
596 - network.c
509,517 - network.c
```

should be removed without question
```
126
807
110-117 - mount.c
```



### AppArmor

confirmed - `mediated_filesystem`, `unconfined`, `cap_ptrace_access_check`, `cap_ptrace_traceme`
```
434, 435
438
447
396
382
369
349
```

questionable
```
448
```

should be removed without question
```
463
477
483
485

```
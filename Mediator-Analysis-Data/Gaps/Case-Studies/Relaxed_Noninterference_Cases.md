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

Common set for relaxed noninterference
```
AppArmor
  "implicit_whitelist": [
    { "file": "security/apparmor/lsm.c", "line": 100 },
    { "file": "security/apparmor/lsm.c", "line": 109 },
    { "file": "security/apparmor/lsm.c", "line": 145 }
  ],

Tomoyo
  "implicit_whitelist": [
    { "file": "security/tomoyo/file.c", "line": 151 },
    { "file": "security/tomoyo/file.c", "line": 814 },
    { "file": "security/tomoyo/mount.c", "line": 94 },
    { "file": "security/tomoyo/mount.c", "line": 102 },
    { "file": "security/tomoyo/mount.c", "line": 122 },
    { "file": "security/tomoyo/mount.c", "line": 132 },
    { "file": "security/tomoyo/mount.c", "line": 138 },
    { "file": "security/tomoyo/mount.c", "line": 147 },
    { "file": "security/tomoyo/network.c", "line": 560 }
  ],

SELinux
  "implicit_whitelist": [
    { "file": "security/selinux/hooks.c", "line": 1728 },
    { "file": "security/selinux/hooks.c", "line": 1731 },
    { "file": "security/selinux/hooks.c", "line": 1823 },
    { "file": "security/selinux/hooks.c", "line": 1827 },
    { "file": "security/selinux/hooks.c", "line": 1841 },
    { "file": "security/selinux/hooks.c", "line": 1942 },
    { "file": "security/selinux/hooks.c", "line": 1959 },
    { "file": "security/selinux/hooks.c", "line": 2008 },
    { "file": "security/selinux/hooks.c", "line": 2917 },
    { "file": "security/selinux/hooks.c", "line": 2919 },
    { "file": "security/selinux/hooks.c", "line": 2922 },
    { "file": "security/selinux/hooks.c", "line": 2948 },
    { "file": "security/selinux/hooks.c", "line": 2951 },
    { "file": "security/selinux/hooks.c", "line": 2959 },
    { "file": "security/selinux/hooks.c", "line": 2963 },
    { "file": "security/selinux/hooks.c", "line": 2990 },
    { "file": "security/selinux/hooks.c", "line": 2995 },
    { "file": "security/selinux/hooks.c", "line": 3000 },
    { "file": "security/selinux/hooks.c", "line": 3328 },
    { "file": "security/selinux/hooks.c", "line": 3597 },
    { "file": "security/selinux/hooks.c", "line": 3608 },
    { "file": "security/selinux/hooks.c", "line": 3639 },
    { "file": "security/selinux/hooks.c", "line": 4039 },
    { "file": "security/selinux/hooks.c", "line": 4076 },
    { "file": "security/selinux/hooks.c", "line": 4138 },
    { "file": "security/selinux/hooks.c", "line": 4166 },
    { "file": "security/selinux/hooks.c", "line": 4315 },
    { "file": "security/selinux/hooks.c", "line": 4319 },
    { "file": "security/selinux/hooks.c", "line": 4323 },
    { "file": "security/selinux/hooks.c", "line": 4344 },
    { "file": "security/selinux/hooks.c", "line": 4355 },
    { "file": "security/selinux/hooks.c", "line": 4398 },
    { "file": "security/selinux/hooks.c", "line": 4405 },
    { "file": "security/selinux/hooks.c", "line": 4409 },
    { "file": "security/selinux/hooks.c", "line": 4415 },
    { "file": "security/selinux/hooks.c", "line": 4421 },
    { "file": "security/selinux/hooks.c", "line": 4717 },
    { "file": "security/selinux/hooks.c", "line": 5070 },
    { "file": "security/selinux/hooks.c", "line": 5244 },
    { "file": "security/selinux/hooks.c", "line": 5254 },
    { "file": "security/selinux/hooks.c", "line": 5258 },
    { "file": "security/selinux/hooks.c", "line": 5284 },
    { "file": "security/selinux/hooks.c", "line": 5567 },
    { "file": "security/selinux/hooks.c", "line": 5590 },
    { "file": "security/selinux/xfrm.c", "line": 89 },
    { "file": "security/selinux/xfrm.c", "line": 90 },
    { "file": "security/selinux/xfrm.c", "line": 91 },
    { "file": "security/selinux/xfrm.c", "line": 95 },
    { "file": "security/selinux/xfrm.c", "line": 99 },
    { "file": "security/selinux/xfrm.c", "line": 108 }
  ],
```


What label should this constant be?
```
CONFIG_LSM_MMAP_MIN_ADDR in selinux_mmap_addr()
```

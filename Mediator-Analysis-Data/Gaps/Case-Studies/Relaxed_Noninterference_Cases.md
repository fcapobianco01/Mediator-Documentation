We record here a series of hook function which returns success in special scenarios.

### SELinux

#### `selinux_sem_semctl`, `selinux_shm_shmctl`, `selinux_msg_queue_msgctl`, 
Returning 0 when `cmd` is not in the set of expected values.

#### **


`selinux_syslog` Should this one be annotated? current are the same, but appear at different places.

`selinux_inode_link` This is a FP because of the implicit assignment in IR at 1797

`file_map_prot_check` Visit this function.

`selinux_file_mprotect` 3328 questionable.

`selinux_quotactl` 2036, explicitly states */\* let the kernel handle invalid cmds \*/*

`selinux_netlink_send` always return 0 on 5069

`selinux_sb_kern_mount` 2614, */\* Allow all mounts performed by the kernel \*/*

`selinux_task_setrlimit` return explicit 0 when the old_limit equals new_limit on their max value.


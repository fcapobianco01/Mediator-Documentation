



| Function                           | sub > obj | sub > op | obj > sub | obj > op | op > sub | op > obj | dyn > stat | in > med | ext > in | ext > med |
| ---------------------------------- | :-------: | :------: | :-------: | :------: | :------: | :------: | :--------: | :------: | :------: | :-------: |
| **_TOMOYO_**                       |           |          |           |          |          |          |            |          |          |           |
| tomoyo_bprm_check_security         |    2/-    |   2/-    |    2/-    |   2/-    |          |          |    4/-     |   9/-    |          |    3/-    |
| tomoyo_file_fcntl                  |    2/-    |   1/-    |    2/-    |   2/-    |   2/-    |   4/-    |    5/-     |   16/-   |          |    4/-    |
| tomoyo_file_ioctl                  |    1/-    |   2/-    |    2/-    |   4/-    |   1/-    |   1/-    |    8/-     |   12/-   |          |    4/-    |
| tomoyo_file_open                   |    2/-    |   2/-    |    2/-    |   2/-    |   1/-    |   1/-    |    5/-     |   9/-    |          |    6/-    |
| tomoyo_path_truncate               |    2/-    |   1/-    |    2/-    |   2/-    |   1/-    |   2/-    |    3/-     |   8/-    |          |    4/-    |
| tomoyo_path_unlink                 |    2/-    |   1/-    |    3/-    |   3/-    |   1/-    |   2/-    |    4/-     |   12/-   |          |    4/-    |
| tomoyo_path_mkdir                  |    1/-    |   2/-    |    3/-    |   6/-    |   2/-    |   2/-    |    10/-    |   16/-   |          |    4/-    |
| tomoyo_path_rmdir                  |    2/-    |   1/-    |    3/-    |   3/-    |   1/-    |   2/-    |    4/-     |   12/-   |          |    4/-    |
| tomoyo_path_symlink                |    2/-    |   1/-    |    4/-    |   4/-    |   1/-    |   2/-    |    5/-     |   16/-   |          |    4/-    |
| tomoyo_path_mknod                  |    2/-    |   6/-    |    4/-    |   12/-   |   5/-    |   5/-    |    14/-    |   26/-   |          |   30/-    |
| tomoyo_path_link                   |    4/-    |   2/-    |    5/-    |   5/-    |   1/-    |   2/-    |    7/-     |   20/-   |          |    4/-    |
| tomoyo_path_rename                 |    4/-    |   2/-    |    6/-    |   6/-    |   1/-    |   2/-    |    8/-     |   24/-   |          |    4/-    |
| tomoyo_inode_getattr               |    2/-    |   1/-    |    3/-    |   3/-    |   1/-    |   2/-    |    4/-     |   12/-   |          |    4/-    |
| tomoyo_path_chmod                  |    1/-    |   2/-    |    2/-    |   4/-    |   2/-    |   2/-    |    8/-     |   12/-   |          |    4/-    |
| tomoyo_path_chown                  |    1/-    |   2/-    |    2/-    |   4/-    |   3/-    |   3/-    |    10/-    |   16/-   |          |    4/-    |
| tomoyo_path_chroot                 |    2/-    |   1/-    |    2/-    |   2/-    |   1/-    |   2/-    |    3/-     |   8/-    |          |    4/-    |
| tomoyo_sb_mount                    |           |          |    4/-    |   8/-    |   2/-    |   4/-    |    12/-    |   20/-   |          |   10/-    |
| tomoyo_sb_umount                   |    2/-    |   1/-    |    2/-    |   2/-    |   1/-    |   2/-    |    3/-     |   8/-    |          |    4/-    |
| tomoyo_sb_pivotroot                |    4/-    |   2/-    |    4/-    |   4/-    |   1/-    |   2/-    |    6/-     |   16/-   |          |    4/-    |
| tomoyo_socket_bind                 |    4/-    |   4/-    |    7/-    |   14/-   |   4/-    |   8/-    |    26/-    |   44/-   |          |   10/-    |
| tomoyo_socket_connect              |    4/-    |   4/-    |    7/-    |   14/-   |   4/-    |   8/-    |    26/-    |   44/-   |          |   10/-    |
| tomoyo_socket_listen               |    4/-    |   4/-    |    7/-    |   14/-   |   4/-    |   8/-    |    26/-    |   44/-   |          |   10/-    |
| tomoyo_socket_sendmsg              |    4/-    |   4/-    |    7/-    |   14/-   |   4/-    |   8/-    |    26/-    |   44/-   |          |   10/-    |
| ------                             |           |          |           |          |          |          |            |          |          |           |
| **_APPARMOR_**                     |           |          |           |          |          |          |            |          |          |           |
| apparmor_path_link                 |           |          |           |          |          |          |            |   3/-    |          |    1/-    |
| apparmor_path_unlink               |    4/-    |          |    2/-    |          |          |          |            |   6/-    |          |    3/-    |
| apparmor_path_rmdir                |    4/-    |          |    2/-    |          |          |          |            |   6/-    |          |    3/-    |
| apparmor_path_symlink              |    2/-    |          |    4/-    |          |          |          |            |   6/-    |          |    9/-    |
| apparmor_path_mkdir                |    2/-    |          |    4/-    |          |          |          |            |   6/-    |          |    9/-    |
| apparmor_path_mknod                |    2/-    |          |    4/-    |          |          |          |            |   9/-    |          |    6/-    |
| apparmor_path_rename               |    8/-    |          |    8/-    |          |          |          |            |   24/-   |          |    6/-    |
| apparmor_path_chmod                |    4/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| apparmor_path_chown                |    4/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| apparmor_path_truncate             |    4/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| apparmor_inode_getattr             |    4/-    |          |    2/-    |          |          |          |            |   6/-    |          |    3/-    |
| apparmor_file_open                 |    2/-    |          |    1/-    |          |   1/-    |   2/-    |            |   9/-    |          |           |
| apparmor_file_permission           |    4/-    |          |    1/-    |          |          |          |    1/-     |   4/-    |          |    3/-    |
| apparmor_mmap_file                 |    4/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| apparmor_file_mprotect             |    4/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| apparmor_file_lock                 |    4/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| apparmor_ptrace_access_check       |    1/-    |          |    1/-    |          |   1/-    |   1/-    |    1/-     |   5/-    |          |    2/-    |
| apparmor_ptrace_traceme            |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| apparmor_capable                   |           |          |    1/-    |          |   1/-    |          |            |   3/-    |          |           |
| apparmor_task_setrlimit            |           |          |    1/-    |          |          |          |            |   3/-    |          |    1/-    |
| ------                             |           |          |           |          |          |          |            |          |          |           |
| **_SELINUX_**                      |           |          |           |          |          |          |            |          |          |           |
| selinux_ptrace_access_check        |    2/-    |          |    2/-    |          |   2/-    |   2/-    |            |   8/-    |          |    4/-    |
| selinux_ptrace_traceme             |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_capget                     |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_capset                     |    1/-    |          |    1/-    |          |          |          |            |   4/-    |          |           |
| selinux_capable                    |    2/-    |          |           |          |   2/-    |   2/-    |    2/-     |   10/-   |          |           |
| selinux_quotactl                   |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_quota_on                   |    4/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_syslog                     |           |          |           |          |          |          |            |          |          |    2/-    |
| selinux_vm_enough_memory           |    4/-    |          |           |          |   2/-    |   2/-    |            |          |          |   10/-    |
| selinux_netlink_send               |    4/-    |   2/-    |    2/-    |   2/-    |          |          |    5/-     |   8/-    |          |    4/-    |
| selinux_sb_kern_mount              |   10/-    |          |    5/-    |          |          |          |            |   10/-   |          |   10/-    |
| selinux_sb_statfs                  |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_mount                      |    6/-    |          |           |          |          |          |            |   3/-    |          |    5/-    |
| selinux_umount                     |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_set_mnt_opts               |    8/-    |          |    8/-    |          |          |          |            |   16/-   |          |    8/-    |
| selinux_inode_create               |    3/-    |          |    9/-    |          |          |          |            |   12/-   |          |    6/-    |
| selinux_inode_link                 |    3/-    |          |    4/-    |          |          |          |            |   10/-   |          |    5/-    |
| selinux_inode_unlink               |    3/-    |          |    4/-    |          |          |          |    1/-     |   10/-   |          |    5/-    |
| selinux_inode_symlink              |    3/-    |          |    9/-    |          |          |          |            |   12/-   |          |    6/-    |
| selinux_inode_mkdir                |    3/-    |          |    9/-    |          |          |          |            |   12/-   |          |    6/-    |
| selinux_inode_rmdir                |    3/-    |          |    4/-    |          |          |          |            |   10/-   |          |    5/-    |
| selinux_inode_mknod                |    3/-    |          |    6/-    |          |          |          |            |   12/-   |          |    6/-    |
| selinux_inode_rename               |    8/-    |   1/-    |   10/-    |   2/-    |          |          |    3/-     |   28/-   |          |   14/-    |
| selinux_inode_readlink             |    4/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_inode_follow_link          |    4/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_inode_permission           |    8/-    |          |    2/-    |          |          |          |            |   6/-    |          |    6/-    |
| selinux_inode_setattr              |    2/-    |          |    1/-    |          |   1/-    |   2/-    |            |   6/-    |          |    3/-    |
| selinux_inode_getattr              |    2/-    |          |    2/-    |          |          |          |            |   6/-    |          |    3/-    |
| selinux_inode_setxattr             |    7/-    |          |    6/-    |          |          |          |            |   15/-   |          |   11/-    |
| selinux_inode_getxattr             |    4/-    |          |    1/-    |          |          |          |            |   6/-    |          |    3/-    |
| selinux_inode_listxattr            |    4/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_inode_removexattr          |    4/-    |          |    2/-    |          |          |          |            |   6/-    |          |    3/-    |
| selinux_inode_getsecurity          |    4/-    |          |           |          |   2/-    |   2/-    |            |          |          |   10/-    |
| selinux_file_permission            |    3/-    |          |    2/-    |          |          |          |            |   5/-    |          |    5/-    |
| selinux_file_ioctl                 |    6/-    |          |    2/-    |          |          |          |            |   5/-    |          |    5/-    |
| selinux_mmap_file                  |    8/-    |          |    3/-    |          |          |          |            |   7/-    |          |    7/-    |
| selinux_mmap_addr                  |    2/-    |          |           |          |          |          |            |          |          |    2/-    |
| selinux_file_mprotect              |   14/-    |          |    6/-    |          |          |          |            |   13/-   |          |   13/-    |
| selinux_file_lock                  |    6/-    |          |    2/-    |          |          |          |            |   5/-    |          |    5/-    |
| selinux_file_fcntl                 |    6/-    |          |    2/-    |          |          |          |            |   5/-    |          |    5/-    |
| selinux_file_send_sigiotask        |    1/-    |          |    1/-    |          |          |          |            |   4/-    |          |           |
| selinux_file_receive               |    6/-    |          |    2/-    |          |          |          |            |   5/-    |          |    5/-    |
| selinux_file_open                  |    2/-    |          |    1/-    |          |   2/-    |   4/-    |            |   12/-   |          |           |
| selinux_task_create                |    1/-    |          |    1/-    |          |          |          |            |          |          |    4/-    |
| selinux_kernel_act_as              |           |          |    1/-    |          |          |          |            |   3/-    |          |    1/-    |
| selinux_kernel_create_files_as     |    2/-    |          |    1/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_kernel_module_request      |           |          |    1/-    |          |          |          |            |   1/-    |          |    1/-    |
| selinux_task_setpgid               |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_task_getpgid               |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_task_getsid                |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_task_setnice               |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_task_setioprio             |    1/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_task_getioprio             |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_task_setrlimit             |    1/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_task_setscheduler          |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_task_getscheduler          |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_task_movememory            |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_task_kill                  |    2/-    |          |    1/-    |          |          |          |    1/-     |   5/-    |          |    3/-    |
| selinux_task_wait                  |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_ipc_permission             |    2/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_msg_queue_alloc_security   |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_msg_queue_associate        |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_msg_queue_msgctl           |    2/-    |          |    2/-    |          |          |          |            |   4/-    |          |    4/-    |
| selinux_msg_queue_msgsnd           |    6/-    |          |    6/-    |          |          |          |            |   12/-   |          |    6/-    |
| selinux_msg_queue_msgrcv           |           |          |    2/-    |          |          |          |            |   6/-    |          |           |
| selinux_shm_alloc_security         |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_shm_associate              |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_shm_shmctl                 |    2/-    |          |    2/-    |          |          |          |    1/-     |   4/-    |          |    4/-    |
| selinux_shm_shmat                  |    2/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_sem_alloc_security         |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_sem_associate              |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_sem_semctl                 |    2/-    |          |    2/-    |          |          |          |    1/-     |   4/-    |          |    4/-    |
| selinux_sem_semop                  |    2/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_getprocattr                |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_setprocattr                |    4/-    |          |    4/-    |          |          |          |            |   8/-    |          |    8/-    |
| selinux_inode_getsecctx            |    4/-    |          |           |          |   2/-    |   2/-    |            |          |          |   10/-    |
| selinux_socket_unix_stream_connect |    2/-    |          |    1/-    |          |          |          |            |   6/-    |          |           |
| selinux_socket_unix_may_send       |    2/-    |          |    1/-    |          |          |          |            |   6/-    |          |           |
| selinux_socket_create              |           |          |    1/-    |          |          |          |            |          |          |    1/-    |
| selinux_socket_bind                |    6/-    |          |    6/-    |          |          |          |            |   18/-   |          |    9/-    |
| selinux_socket_connect             |    4/-    |   1/-    |    4/-    |   2/-    |          |          |    3/-     |   14/-   |          |    7/-    |
| selinux_socket_listen              |    2/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_socket_accept              |    2/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_socket_sendmsg             |    2/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_socket_recvmsg             |    2/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_socket_getsockname         |    2/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_socket_getpeername         |    2/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_socket_getsockopt          |    2/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_socket_setsockopt          |    2/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_socket_shutdown            |    2/-    |          |    1/-    |          |          |          |            |   3/-    |          |    3/-    |
| selinux_socket_sock_rcv_skb        |    5/-    |          |    4/-    |          |          |          |            |   18/-   |          |           |
| selinux_secmark_relabel_packet     |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_tun_dev_create             |    1/-    |          |           |          |          |          |            |          |          |    2/-    |
| selinux_tun_dev_attach_queue       |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_tun_dev_open               |    2/-    |          |    2/-    |          |          |          |            |   4/-    |          |    4/-    |
| selinux_xfrm_policy_alloc          |    1/-    |          |    3/-    |          |          |          |            |   6/-    |          |    2/-    |
| selinux_xfrm_policy_delete         |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_xfrm_state_alloc           |    1/-    |          |    3/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_xfrm_state_delete          |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_xfrm_policy_lookup         |           |          |           |          |          |          |            |   2/-    |          |           |
| selinux_xfrm_state_pol_flow_match  |    1/-    |          |    2/-    |          |          |          |            |   6/-    |          |           |
| selinux_key_permission             |           |          |    1/-    |          |          |          |    1/-     |   4/-    |          |           |
| ------                             |           |          |           |          |          |          |            |          |          |           |

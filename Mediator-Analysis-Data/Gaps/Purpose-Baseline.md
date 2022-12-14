



| Function                           | sub > obj | sub > op | obj > sub | obj > op | op > sub | op > obj | dyn > stat | in > med | ext > in | ext > med |
| ---------------------------------- | :-------: | :------: | :-------: | :------: | :------: | :------: | :--------: | :------: | :------: | :-------: |
| **_TOMOYO_**                       |           |          |           |          |          |          |            |          |          |           |
| tomoyo_bprm_check_security         |    2/-    |   2/-    |    2/-    |   2/-    |          |          |    4/-     |   6/-    |          |    3/-    |
| tomoyo_file_fcntl                  |    1/-    |   1/-    |    1/-    |   1/-    |   1/-    |   1/-    |    3/-     |   6/-    |          |    3/-    |
| tomoyo_file_ioctl                  |    1/-    |   1/-    |    1/-    |   1/-    |   2/-    |   2/-    |    4/-     |   9/-    |          |    3/-    |
| tomoyo_file_open                   |    2/-    |   2/-    |    2/-    |   2/-    |   1/-    |   1/-    |    5/-     |   9/-    |          |    3/-    |
| tomoyo_path_truncate               |    1/-    |   1/-    |    1/-    |   1/-    |   1/-    |   1/-    |    2/-     |   3/-    |          |    3/-    |
| tomoyo_path_unlink                 |    1/-    |   1/-    |    2/-    |   2/-    |   1/-    |   1/-    |    3/-     |   6/-    |          |    3/-    |
| tomoyo_path_mkdir                  |    1/-    |   1/-    |    2/-    |   2/-    |   2/-    |   2/-    |    4/-     |   9/-    |          |    3/-    |
| tomoyo_path_rmdir                  |    1/-    |   1/-    |    2/-    |   2/-    |   1/-    |   1/-    |    3/-     |   6/-    |          |    3/-    |
| tomoyo_path_symlink                |    1/-    |   1/-    |    3/-    |   3/-    |   1/-    |   1/-    |    4/-     |   9/-    |          |    3/-    |
| tomoyo_path_mknod                  |    2/-    |   2/-    |    2/-    |   2/-    |   4/-    |   4/-    |    8/-     |   12/-   |          |    6/-    |
| tomoyo_path_link                   |    3/-    |   3/-    |    3/-    |   3/-    |   1/-    |   1/-    |    6/-     |   9/-    |          |    3/-    |
| tomoyo_path_rename                 |    3/-    |   3/-    |    4/-    |   4/-    |   1/-    |   1/-    |    7/-     |   12/-   |          |    3/-    |
| tomoyo_inode_getattr               |    1/-    |   1/-    |    2/-    |   2/-    |   1/-    |   1/-    |    3/-     |   6/-    |          |    3/-    |
| tomoyo_path_chmod                  |    1/-    |   1/-    |    1/-    |   1/-    |   2/-    |   2/-    |    3/-     |   6/-    |          |    3/-    |
| tomoyo_path_chown                  |    1/-    |   1/-    |    3/-    |   3/-    |   1/-    |   1/-    |    4/-     |   9/-    |          |    3/-    |
| tomoyo_path_chroot                 |    1/-    |   1/-    |    1/-    |   1/-    |   1/-    |   1/-    |    2/-     |   3/-    |          |    3/-    |
| tomoyo_sb_mount                    |           |          |    2/-    |   2/-    |   2/-    |   2/-    |    4/-     |   12/-   |          |           |
| tomoyo_sb_umount                   |    1/-    |   1/-    |    1/-    |   1/-    |   1/-    |   1/-    |    2/-     |   3/-    |          |    3/-    |
| tomoyo_sb_pivotroot                |    3/-    |   3/-    |    2/-    |   2/-    |   1/-    |   1/-    |    5/-     |   6/-    |          |    3/-    |
| tomoyo_socket_bind                 |    2/-    |   2/-    |    6/-    |   6/-    |   4/-    |   4/-    |    12/-    |   24/-   |          |    6/-    |
| tomoyo_socket_connect              |    2/-    |   2/-    |    6/-    |   6/-    |   4/-    |   4/-    |    12/-    |   24/-   |          |    6/-    |
| tomoyo_socket_listen               |    2/-    |   2/-    |    6/-    |   6/-    |   4/-    |   4/-    |    12/-    |   24/-   |          |    6/-    |
| tomoyo_socket_sendmsg              |    2/-    |   2/-    |    6/-    |   6/-    |   4/-    |   4/-    |    12/-    |   24/-   |          |    6/-    |
| ------                             |           |          |           |          |          |          |            |          |          |           |
| **_APPARMOR_**                     |           |          |           |          |          |          |            |          |          |           |
| apparmor_path_link                 |           |          |           |          |          |          |            |   3/-    |          |    1/-    |
| apparmor_path_unlink               |    2/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| apparmor_path_rmdir                |    2/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| apparmor_path_symlink              |    1/-    |          |    4/-    |          |          |          |            |   4/-    |          |    6/-    |
| apparmor_path_mkdir                |    1/-    |          |    4/-    |          |          |          |            |   4/-    |          |    6/-    |
| apparmor_path_mknod                |    1/-    |          |    4/-    |          |          |          |            |   6/-    |          |    4/-    |
| apparmor_path_rename               |    2/-    |          |    4/-    |          |          |          |            |   8/-    |          |    2/-    |
| apparmor_path_chmod                |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| apparmor_path_chown                |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| apparmor_path_truncate             |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| apparmor_inode_getattr             |    2/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| apparmor_file_open                 |    1/-    |          |    1/-    |          |   1/-    |   1/-    |            |   6/-    |          |           |
| apparmor_file_permission           |    2/-    |          |    1/-    |          |          |          |    1/-     |   3/-    |          |    2/-    |
| apparmor_mmap_file                 |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| apparmor_file_mprotect             |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| apparmor_file_lock                 |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| apparmor_ptrace_access_check       |    1/-    |          |    1/-    |          |   1/-    |   1/-    |    1/-     |   5/-    |          |    2/-    |
| apparmor_ptrace_traceme            |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| apparmor_capable                   |           |          |           |          |          |          |            |   1/-    |          |           |
| apparmor_task_setrlimit            |           |          |           |          |          |          |            |          |          |    1/-    |
| ------                             |           |          |           |          |          |          |            |          |          |           |
| **_SELINUX_**                      |           |          |           |          |          |          |            |          |          |           |
| selinux_ptrace_access_check        |    1/-    |          |    1/-    |          |   1/-    |   1/-    |            |   4/-    |          |    2/-    |
| selinux_ptrace_traceme             |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_capget                     |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_capset                     |    1/-    |          |    1/-    |          |          |          |            |   4/-    |          |           |
| selinux_capable                    |    1/-    |          |           |          |   1/-    |   1/-    |    1/-     |   5/-    |          |           |
| selinux_quotactl                   |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_quota_on                   |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_syslog                     |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_vm_enough_memory           |    2/-    |          |           |          |   1/-    |   1/-    |            |          |          |    5/-    |
| selinux_netlink_send               |    2/-    |   2/-    |    2/-    |   2/-    |          |          |    5/-     |   6/-    |          |    3/-    |
| selinux_sb_kern_mount              |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_sb_statfs                  |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_mount                      |    2/-    |          |           |          |          |          |            |   1/-    |          |    2/-    |
| selinux_umount                     |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_set_mnt_opts               |    2/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_inode_create               |    1/-    |          |    3/-    |          |          |          |            |   6/-    |          |    2/-    |
| selinux_inode_link                 |    1/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_inode_unlink               |    1/-    |          |    2/-    |          |          |          |    1/-     |   4/-    |          |    2/-    |
| selinux_inode_symlink              |    1/-    |          |    3/-    |          |          |          |            |   6/-    |          |    2/-    |
| selinux_inode_mkdir                |    1/-    |          |    3/-    |          |          |          |            |   6/-    |          |    2/-    |
| selinux_inode_rmdir                |    1/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_inode_mknod                |    1/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_inode_rename               |    1/-    |   1/-    |    2/-    |   2/-    |          |          |    3/-     |   6/-    |          |    3/-    |
| selinux_inode_readlink             |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_inode_follow_link          |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_inode_permission           |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_inode_setattr              |    1/-    |          |    1/-    |          |   1/-    |   1/-    |            |   4/-    |          |    2/-    |
| selinux_inode_getattr              |    1/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_inode_setxattr             |    1/-    |          |    3/-    |          |          |          |            |   6/-    |          |    2/-    |
| selinux_inode_getxattr             |    2/-    |          |    1/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_inode_listxattr            |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_inode_removexattr          |    2/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_inode_getsecurity          |    2/-    |          |           |          |   1/-    |   1/-    |            |          |          |    5/-    |
| selinux_file_permission            |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_file_ioctl                 |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_mmap_file                  |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_mmap_addr                  |    1/-    |          |           |          |          |          |            |          |          |    1/-    |
| selinux_file_mprotect              |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_file_lock                  |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_file_fcntl                 |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_file_send_sigiotask        |    1/-    |          |    1/-    |          |          |          |            |   4/-    |          |           |
| selinux_file_receive               |    2/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_file_open                  |    1/-    |          |    1/-    |          |   2/-    |   2/-    |            |   8/-    |          |           |
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
| selinux_task_kill                  |    1/-    |          |    1/-    |          |          |          |    1/-     |   4/-    |          |    2/-    |
| selinux_task_wait                  |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_ipc_permission             |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_msg_queue_alloc_security   |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_msg_queue_associate        |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_msg_queue_msgctl           |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_msg_queue_msgsnd           |    2/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_msg_queue_msgrcv           |           |          |    1/-    |          |          |          |            |   4/-    |          |           |
| selinux_shm_alloc_security         |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_shm_associate              |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_shm_shmctl                 |    1/-    |          |    1/-    |          |          |          |    1/-     |   2/-    |          |    2/-    |
| selinux_shm_shmat                  |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_sem_alloc_security         |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_sem_associate              |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_sem_semctl                 |    1/-    |          |    1/-    |          |          |          |    1/-     |   2/-    |          |    2/-    |
| selinux_sem_semop                  |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_getprocattr                |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_setprocattr                |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_inode_getsecctx            |    2/-    |          |           |          |   1/-    |   1/-    |            |          |          |    5/-    |
| selinux_socket_unix_stream_connect |    1/-    |          |    1/-    |          |          |          |            |   4/-    |          |           |
| selinux_socket_unix_may_send       |    1/-    |          |    1/-    |          |          |          |            |   4/-    |          |           |
| selinux_socket_create              |           |          |           |          |          |          |            |          |          |    1/-    |
| selinux_socket_bind                |    1/-    |          |    2/-    |          |          |          |            |   4/-    |          |    2/-    |
| selinux_socket_connect             |    1/-    |   1/-    |    2/-    |   2/-    |          |          |    3/-     |   6/-    |          |    3/-    |
| selinux_socket_listen              |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_socket_accept              |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_socket_sendmsg             |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_socket_recvmsg             |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_socket_getsockname         |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_socket_getpeername         |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_socket_getsockopt          |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_socket_setsockopt          |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_socket_shutdown            |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_socket_sock_rcv_skb        |    1/-    |          |    1/-    |          |          |          |            |   4/-    |          |           |
| selinux_secmark_relabel_packet     |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_tun_dev_create             |    1/-    |          |           |          |          |          |            |          |          |    2/-    |
| selinux_tun_dev_attach_queue       |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_tun_dev_open               |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |    2/-    |
| selinux_xfrm_policy_alloc          |    1/-    |          |    3/-    |          |          |          |            |   6/-    |          |           |
| selinux_xfrm_policy_delete         |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |           |
| selinux_xfrm_state_alloc           |    1/-    |          |    3/-    |          |          |          |            |   4/-    |          |           |
| selinux_xfrm_state_delete          |    1/-    |          |    1/-    |          |          |          |            |   2/-    |          |           |
| selinux_xfrm_policy_lookup         |           |          |           |          |          |          |            |   2/-    |          |           |
| selinux_xfrm_state_pol_flow_match  |    1/-    |          |    2/-    |          |          |          |            |   6/-    |          |           |
| selinux_key_permission             |           |          |    1/-    |          |          |          |    1/-     |   4/-    |          |           |
| ------                             |           |          |           |          |          |          |            |          |          |           |

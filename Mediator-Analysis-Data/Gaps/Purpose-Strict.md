



| Function                           | sub > obj | sub > op | obj > sub | obj > op | op > sub | op > obj | dyn > stat | in > med | ext > in | ext > med |
| ---------------------------------- | :-------: | :------: | :-------: | :------: | :------: | :------: | :--------: | :------: | :------: | :-------: |
| **_TOMOYO_**                       |           |          |           |          |          |          |            |          |          |           |
| tomoyo_bprm_check_security         |    -/2    |   -/2    |           |   -/2    |          |          |    -/4     |   2/5    |          |    1/2    |
| tomoyo_file_fcntl                  |    -/1    |   -/1    |           |   -/2    |   -/5    |   -/5    |    1/5     |   2/11   |          |    2/7    |
| tomoyo_file_ioctl                  |    -/1    |   -/2    |           |   -/2    |          |          |    1/4     |   2/3    |          |    1/3    |
| tomoyo_file_open                   |    -/2    |   -/2    |           |   -/2    |   -/1    |   -/1    |    1/4     |   2/5    |          |    2/4    |
| tomoyo_path_truncate               |    -/2    |   -/1    |           |   -/2    |          |   -/2    |    -/3     |   1/5    |          |    1/3    |
| tomoyo_path_unlink                 |    -/2    |   -/1    |           |   -/3    |          |   -/2    |    -/4     |   1/8    |          |    1/3    |
| tomoyo_path_mkdir                  |    -/1    |   -/2    |           |   -/2    |          |   -/1    |    1/4     |   2/3    |          |    2/3    |
| tomoyo_path_rmdir                  |    -/2    |   -/1    |           |   -/3    |          |   -/2    |    -/4     |   1/8    |          |    1/3    |
| tomoyo_path_symlink                |    -/2    |   -/1    |           |   -/4    |          |   -/2    |    -/5     |   1/11   |          |    1/3    |
| tomoyo_path_mknod                  |    -/2    |   -/6    |           |   -/2    |          |   -/2    |    -/6     |   4/3    |          |   6/14    |
| tomoyo_path_link                   |    -/4    |   -/2    |           |          |          |   -/2    |    -/2     |   2/-    |          |    1/3    |
| tomoyo_path_rename                 |    -/4    |   -/2    |           |          |          |   -/2    |    -/2     |   2/-    |          |    1/3    |
| tomoyo_inode_getattr               |    -/2    |   -/1    |           |   -/3    |          |   -/2    |    -/4     |   1/8    |          |    1/3    |
| tomoyo_path_chmod                  |    -/1    |   -/2    |           |   -/2    |          |   -/1    |    1/4     |   2/3    |          |    2/3    |
| tomoyo_path_chown                  |    -/1    |   -/2    |    -/2    |   -/4    |   -/5    |   -/5    |    2/8     |   3/13   |          |   1/11    |
| tomoyo_path_chroot                 |    -/2    |   -/1    |           |   -/2    |          |   -/2    |    -/3     |   1/5    |          |    1/3    |
| tomoyo_sb_mount                    |           |          |           |   -/4    |          |   -/2    |    1/6     |   2/8    |          |    1/4    |
| tomoyo_sb_umount                   |    -/2    |   -/1    |           |   -/2    |          |   -/2    |    -/3     |   1/5    |          |    1/3    |
| tomoyo_sb_pivotroot                |    -/4    |   -/2    |           |          |          |   -/2    |    -/2     |   2/-    |          |    1/3    |
| tomoyo_socket_bind                 |    -/4    |   -/4    |    -/3    |   -/10   |   -/4    |   -/8    |    4/18    |   7/28   |          |    2/8    |
| tomoyo_socket_connect              |    -/4    |   -/4    |    -/3    |   -/10   |   -/4    |   -/8    |    4/18    |   7/28   |          |    2/8    |
| tomoyo_socket_listen               |    -/4    |   -/4    |    -/3    |   -/10   |   -/4    |   -/8    |    4/18    |   7/28   |          |    2/8    |
| tomoyo_socket_sendmsg              |    -/4    |   -/4    |    -/3    |   -/10   |   -/4    |   -/8    |    4/18    |   7/28   |          |    2/8    |
| ------                             |           |          |           |          |          |          |            |          |          |           |
| **_APPARMOR_**                     |           |          |           |          |          |          |            |          |          |           |
| apparmor_path_link                 |           |          |    -/1    |          |          |          |            |   3/1    |          |    1/-    |
| apparmor_path_unlink               |           |          |    -/2    |          |          |          |            |   3/3    |          |    1/-    |
| apparmor_path_rmdir                |           |          |    -/3    |          |          |          |            |   3/3    |          |    1/3    |
| apparmor_path_symlink              |           |          |    2/1    |          |          |          |            |   2/1    |          |    5/-    |
| apparmor_path_mkdir                |           |          |    2/2    |          |          |          |            |   2/1    |          |    5/2    |
| apparmor_path_mknod                |           |          |    2/2    |          |          |          |            |   4/1    |          |    3/2    |
| apparmor_path_rename               |    -/8    |          |    -/4    |          |   -/2    |   -/4    |            |   12/4   |          |   2/10    |
| apparmor_path_chmod                |           |          |    -/2    |          |          |          |            |   2/1    |          |    1/3    |
| apparmor_path_chown                |           |          |    -/2    |          |          |          |            |   2/1    |          |    1/1    |
| apparmor_path_truncate             |           |          |    -/2    |          |          |          |            |   2/1    |          |    1/1    |
| apparmor_inode_getattr             |           |          |    -/2    |          |          |          |            |   3/1    |          |    1/3    |
| apparmor_file_open                 |    -/1    |   -/1    |    -/1    |   -/1    |   -/5    |   4/1    |    -/2     |   1/3    |          |   10/13   |
| apparmor_file_permission           |    -/4    |          |    -/2    |          |          |   -/2    |    1/-     |   3/3    |          |    1/5    |
| apparmor_mmap_file                 |    -/4    |          |    -/2    |   -/1    |          |   -/16   |    -/3     |   2/8    |          |   3/21    |
| apparmor_file_mprotect             |    -/4    |          |    -/2    |   -/1    |          |   -/16   |    -/3     |   2/5    |          |   3/24    |
| apparmor_file_lock                 |    -/4    |          |    -/2    |          |          |   -/6    |    -/1     |   2/4    |          |   2/10    |
| apparmor_ptrace_access_check       |           |          |    -/1    |          |   -/1    |          |    1/-     |   2/2    |          |    1/-    |
| apparmor_ptrace_traceme            |    -/1    |          |           |          |          |          |            |   1/1    |          |    1/-    |
| apparmor_capable                   |           |          |    -/1    |          |   -/1    |          |            |   1/2    |          |           |
| apparmor_task_setrlimit            |    -/2    |          |           |          |          |          |            |   2/-    |          |    1/1    |
| ------                             |           |          |           |          |          |          |            |          |          |           |
| **_SELINUX_**                      |           |          |           |          |          |          |            |          |          |           |
| selinux_ptrace_access_check        |           |          |    -/2    |          |   -/4    |   -/4    |            |   2/6    |          |    2/4    |
| selinux_ptrace_traceme             |    -/1    |          |           |          |          |          |            |   1/1    |          |    1/-    |
| selinux_capget                     |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_capset                     |    1/-    |          |    1/-    |          |          |          |            |   4/-    |          |           |
| selinux_capable                    |    2/2    |   -/2    |           |          |   -/2    |   -/6    |    2/2     |   6/10   |          |    2/2    |
| selinux_quotactl                   |           |          |    -/1    |          |   -/1    |   -/1    |            |   1/3    |          |    1/-    |
| selinux_quota_on                   |           |          |    -/1    |          |          |          |            |   2/1    |          |    1/-    |
| selinux_syslog                     |           |          |           |          |   -/1    |          |            |   -/1    |          |    2/-    |
| selinux_vm_enough_memory           |    4/4    |   -/4    |           |          |   2/2    |   2/8    |    -/4     |          |          |   12/16   |
| selinux_netlink_send               |           |          |    -/2    |   -/2    |   -/2    |   -/4    |    1/2     |   2/6    |          |    1/4    |
| selinux_sb_kern_mount              |    8/2    |          |    4/1    |          |  62/38   |  62/38   |            |   8/2    |          |  122/78   |
| selinux_sb_statfs                  |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_mount                      |           |          |    -/1    |          |   -/2    |   -/3    |            |   3/1    |          |    2/5    |
| selinux_umount                     |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_set_mnt_opts               |    6/2    |          |    6/2    |          |  46/22   |  46/22   |            |   12/4   |          |   86/42   |
| selinux_inode_create               |    1/1    |          |    -/3    |          |          |          |            |   2/5    |          |    4/1    |
| selinux_inode_link                 |           |          |           |          |          |   -/2    |            |   3/-    |          |    2/-    |
| selinux_inode_unlink               |           |          |           |          |          |   -/2    |    1/1     |   3/-    |          |    2/-    |
| selinux_inode_symlink              |    1/1    |          |    -/3    |          |          |          |            |   2/5    |          |    4/1    |
| selinux_inode_mkdir                |    1/1    |          |    -/3    |          |          |          |            |   2/5    |          |    4/1    |
| selinux_inode_rmdir                |           |          |           |          |          |   -/2    |            |   3/-    |          |    2/-    |
| selinux_inode_mknod                |    1/1    |          |    -/2    |          |          |          |            |   2/5    |          |    4/1    |
| selinux_inode_rename               |           |          |           |   2/2    |          |          |    2/2     |   14/4   |          |    5/-    |
| selinux_inode_readlink             |           |          |    -/1    |          |          |          |            |   2/1    |          |    1/-    |
| selinux_inode_follow_link          |           |          |    -/1    |          |          |          |            |   2/1    |          |    1/-    |
| selinux_inode_permission           |           |          |    -/2    |   -/2    |   2/14   |   2/16   |    -/4     |   4/12   |          |   6/38    |
| selinux_inode_setattr              |           |          |    -/1    |          |   -/2    |   -/4    |    -/1     |   2/5    |          |    1/5    |
| selinux_inode_getattr              |           |          |    -/1    |          |          |          |            |   2/1    |          |    1/-    |
| selinux_inode_setxattr             |    -/1    |          |   -/12    |          |   6/28   |  12/28   |            |   6/19   |          |   21/58   |
| selinux_inode_getxattr             |           |          |    -/1    |          |          |          |            |   3/1    |          |    1/-    |
| selinux_inode_listxattr            |           |          |    -/1    |          |          |          |            |   2/1    |          |    1/-    |
| selinux_inode_removexattr          |           |          |    -/2    |          |   2/3    |   -/10   |            |   2/4    |          |   3/13    |
| selinux_inode_getsecurity          |    4/4    |   -/4    |           |          |   -/2    |   -/6    |    -/4     |          |          |   8/12    |
| selinux_file_permission            |    -/6    |   -/2    |    -/2    |   -/1    |   -/13   |   -/24   |    -/4     |   3/9    |          |   4/46    |
| selinux_file_ioctl                 |    4/2    |          |    -/1    |          |   -/5    |   4/5    |            |   3/6    |          |    9/3    |
| selinux_mmap_file                  |    2/6    |          |    -/3    |   -/1    |   -/31   |   -/42   |    -/4     |   3/29   |          |   6/49    |
| selinux_mmap_addr                  |    2/-    |          |    -/1    |          |   -/1    |   -/1    |            |   -/2    |          |    2/2    |
| selinux_file_mprotect              |    6/8    |   -/2    |    -/6    |   -/1    |   5/49   |   6/57   |    -/5     |   4/38   |          |   22/90   |
| selinux_file_lock                  |    -/6    |          |    -/1    |          |   -/1    |   -/2    |            |   3/1    |          |    2/3    |
| selinux_file_fcntl                 |    -/6    |          |    -/2    |          |   -/9    |   -/14   |            |   3/12   |          |   2/13    |
| selinux_file_send_sigiotask        |           |          |           |          |          |          |    -/1     |   2/1    |          |           |
| selinux_file_receive               |    -/6    |          |    -/1    |   -/1    |   -/6    |   -/12   |    -/1     |   3/2    |          |   4/14    |
| selinux_file_open                  |           |          |    -/1    |          |          |          |    -/2     |   3/3    |          |    1/2    |
| selinux_task_create                |    1/-    |          |    1/-    |          |          |          |            |          |          |    4/-    |
| selinux_kernel_act_as              |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_kernel_create_files_as     |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_kernel_module_request      |           |          |           |          |          |          |            |          |          |    1/-    |
| selinux_task_setpgid               |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_task_getpgid               |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_task_getsid                |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_task_setnice               |           |          |    -/1    |          |          |          |            |   1/1    |          |    1/-    |
| selinux_task_setioprio             |           |          |    -/2    |          |          |          |            |   1/3    |          |    1/-    |
| selinux_task_getioprio             |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_task_setrlimit             |           |          |    -/3    |          |          |          |            |   1/5    |          |    1/-    |
| selinux_task_setscheduler          |           |          |    -/1    |          |          |          |            |   1/1    |          |    1/-    |
| selinux_task_getscheduler          |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_task_movememory            |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_task_kill                  |    -/2    |          |           |          |          |          |    1/2     |   4/5    |          |    1/-    |
| selinux_task_wait                  |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_ipc_permission             |           |          |           |          |   -/7    |   -/14   |    -/1     |   2/4    |          |    1/8    |
| selinux_msg_queue_alloc_security   |    1/-    |          |           |          |          |   1/-    |            |   1/-    |          |    3/-    |
| selinux_msg_queue_associate        |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_msg_queue_msgctl           |           |          |           |          |   -/2    |   -/2    |    -/1     |   2/5    |          |    2/-    |
| selinux_msg_queue_msgsnd           |    -/6    |          |    1/1    |          |   -/1    |   -/3    |            |   4/4    |          |    2/4    |
| selinux_msg_queue_msgrcv           |           |          |           |          |          |          |            |   4/-    |          |           |
| selinux_shm_alloc_security         |    1/-    |          |           |          |          |   1/-    |            |   1/-    |          |    3/-    |
| selinux_shm_associate              |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_shm_shmctl                 |           |          |           |          |   -/2    |   -/2    |    1/1     |   2/5    |          |    2/-    |
| selinux_shm_shmat                  |           |          |           |          |          |          |            |   2/-    |          |    1/-    |
| selinux_sem_alloc_security         |    1/-    |          |           |          |          |   1/-    |            |   1/-    |          |    3/-    |
| selinux_sem_associate              |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_sem_semctl                 |           |          |           |          |   -/2    |   -/2    |    1/1     |   2/5    |          |    2/-    |
| selinux_sem_semop                  |           |          |           |          |          |          |            |   2/-    |          |    1/-    |
| selinux_getprocattr                |    -/1    |          |    -/1    |          |          |          |            |   1/1    |          |    1/1    |
| selinux_setprocattr                |    -/4    |          |    2/2    |          |   4/16   |   6/14   |            |   3/5    |          |   11/37   |
| selinux_inode_getsecctx            |    4/4    |   -/4    |           |          |   -/2    |   -/6    |    -/4     |          |          |   8/12    |
| selinux_socket_unix_stream_connect |           |          |           |          |          |          |            |   3/-    |          |           |
| selinux_socket_unix_may_send       |           |          |           |          |          |          |            |   3/-    |          |           |
| selinux_socket_create              |    1/1    |          |    -/1    |          |          |          |            |          |          |    2/-    |
| selinux_socket_bind                |           |          |    2/2    |   -/2    |   6/2    |   -/16   |    -/2     |   6/10   |          |   7/22    |
| selinux_socket_connect             |           |          |    1/4    |   2/3    |   1/1    |   -/4    |    1/2     |   5/9    |          |    2/7    |
| selinux_socket_listen              |           |          |           |          |          |          |            |   2/-    |          |    1/-    |
| selinux_socket_accept              |           |          |           |          |          |          |            |   2/-    |          |    1/-    |
| selinux_socket_sendmsg             |           |          |           |          |          |          |            |   2/-    |          |    1/-    |
| selinux_socket_recvmsg             |           |          |           |          |          |          |            |   2/-    |          |    1/-    |
| selinux_socket_getsockname         |           |          |           |          |          |          |            |   2/-    |          |    1/-    |
| selinux_socket_getpeername         |           |          |           |          |          |          |            |   2/-    |          |    1/-    |
| selinux_socket_getsockopt          |           |          |           |          |          |          |            |   2/-    |          |    1/-    |
| selinux_socket_setsockopt          |           |          |           |          |          |          |            |   2/-    |          |    1/-    |
| selinux_socket_shutdown            |           |          |           |          |          |          |            |   2/-    |          |    1/-    |
| selinux_socket_sock_rcv_skb        |    -/6    |          |    -/3    |          |   2/21   |   -/36   |            |   7/14   |          |   5/57    |
| selinux_secmark_relabel_packet     |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_tun_dev_create             |    1/-    |          |           |          |          |          |            |          |          |    2/-    |
| selinux_tun_dev_attach_queue       |           |          |           |          |          |          |            |   1/-    |          |    1/-    |
| selinux_tun_dev_open               |    2/-    |          |           |          |          |          |            |   1/-    |          |    4/-    |
| selinux_xfrm_policy_alloc          |           |          |    -/3    |          |          |          |            |   2/4    |          |    1/-    |
| selinux_xfrm_policy_delete         |           |          |    -/1    |          |          |          |            |   1/1    |          |    1/-    |
| selinux_xfrm_state_alloc           |           |          |    -/3    |          |          |          |            |   1/3    |          |    1/-    |
| selinux_xfrm_state_delete          |           |          |    -/1    |          |          |          |            |   1/1    |          |    1/-    |
| selinux_xfrm_policy_lookup         |           |          |           |          |          |          |            |   2/-    |          |           |
| selinux_xfrm_state_pol_flow_match  |           |          |    -/2    |          |          |          |            |   2/3    |          |           |
| selinux_key_permission             |           |          |           |          |   -/1    |   -/1    |    1/-     |   3/2    |          |           |
| ------                             |           |          |           |          |          |          |            |          |          |           |

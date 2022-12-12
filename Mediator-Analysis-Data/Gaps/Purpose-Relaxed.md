 : Explicit flows detected

 : Implicit flows detected

| Function                           | sub :arrow_right: obj | sub :arrow_right:op  | obj :arrow_right: sub | obj :arrow_right: op | op:arrow_right: sub  | op :arrow_right: obj |  No cross-domain   |
| ---------------------------------- | :-------------------: | :------------------: | :-------------------: | :------------------: | :------------------: | :------------------: | :----------------: |
| **_TOMOYO_**                       |                       |                      |                       |                      |                      |                      |                    |
| tomoyo_bprm_check_security         | :large_blue_diamond:  | :large_blue_diamond: |                       |                      |                      |                      |                    |
| tomoyo_file_fcntl                  | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond: | :large_blue_diamond: |                    |
| tomoyo_file_ioctl                  | :large_blue_diamond:  | :large_blue_diamond: |                       | :large_blue_diamond: |                      | :large_blue_diamond: |                    |
| tomoyo_file_open                   | :large_blue_diamond:  | :large_blue_diamond: |                       |                      | :large_blue_diamond: | :large_blue_diamond: |                    |
| tomoyo_path_truncate               | :large_blue_diamond:  | :large_blue_diamond: |                       |                      |                      | :large_blue_diamond: |                    |
| tomoyo_path_unlink                 | :large_blue_diamond:  | :large_blue_diamond: |                       |                      |                      | :large_blue_diamond: |                    |
| tomoyo_path_mkdir                  | :large_blue_diamond:  | :large_blue_diamond: |                       | :large_blue_diamond: |                      | :large_blue_diamond: |                    |
| tomoyo_path_rmdir                  | :large_blue_diamond:  | :large_blue_diamond: |                       |                      |                      | :large_blue_diamond: |                    |
| tomoyo_path_symlink                | :large_blue_diamond:  | :large_blue_diamond: |                       |                      |                      | :large_blue_diamond: |                    |
| tomoyo_path_mknod                  | :large_blue_diamond:  | :large_blue_diamond: |                       | :large_blue_diamond: |                      | :large_blue_diamond: |                    |
| tomoyo_path_link                   | :large_blue_diamond:  | :large_blue_diamond: |                       |                      |                      | :large_blue_diamond: |                    |
| tomoyo_path_rename                 | :large_blue_diamond:  | :large_blue_diamond: |                       |                      |                      | :large_blue_diamond: |                    |
| tomoyo_inode_getattr               | :large_blue_diamond:  | :large_blue_diamond: |                       |                      |                      | :large_blue_diamond: |                    |
| tomoyo_path_chmod                  | :large_blue_diamond:  | :large_blue_diamond: |                       | :large_blue_diamond: |                      | :large_blue_diamond: |                    |
| tomoyo_path_chown                  | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond: | :large_blue_diamond: |                    |
| tomoyo_path_chroot                 | :large_blue_diamond:  | :large_blue_diamond: |                       |                      |                      | :large_blue_diamond: |                    |
| tomoyo_sb_mount                    |                       |                      |                       |                      |                      | :large_blue_diamond: |                    |
| tomoyo_sb_umount                   | :large_blue_diamond:  | :large_blue_diamond: |                       |                      |                      | :large_blue_diamond: |                    |
| tomoyo_sb_pivotroot                | :large_blue_diamond:  | :large_blue_diamond: |                       |                      |                      | :large_blue_diamond: |                    |
| tomoyo_socket_bind                 | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond: | :large_blue_diamond: |                    |
| tomoyo_socket_connect              | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond: | :large_blue_diamond: |                    |
| tomoyo_socket_listen               | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond: | :large_blue_diamond: |                    |
| tomoyo_socket_sendmsg              | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond: | :large_blue_diamond: |                    |
| ------                             |                       |                      |                       |                      |                      |                      |                    |
| **_APPARMOR_**                     |                       |                      |                       |                      |                      |                      |                    |
| apparmor_path_link                 |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| apparmor_path_unlink               |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| apparmor_path_rmdir                |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| apparmor_path_symlink              |                       |                      |     :red_circle:      |                      |                      |                      |                    |
| apparmor_path_mkdir                |                       |                      |     :red_circle:      |                      |                      |                      |                    |
| apparmor_path_mknod                |                       |                      |     :red_circle:      |                      |                      |                      |                    |
| apparmor_path_rename               | :large_blue_diamond:  |                      | :large_blue_diamond:  |                      | :large_blue_diamond: | :large_blue_diamond: |                    |
| apparmor_path_chmod                |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| apparmor_path_chown                |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| apparmor_path_truncate             |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| apparmor_inode_getattr             |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| apparmor_file_open                 | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond: |     :red_circle:     |                    |
| apparmor_file_permission           | :large_blue_diamond:  |                      | :large_blue_diamond:  |                      |                      | :large_blue_diamond: |                    |
| apparmor_mmap_file                 | :large_blue_diamond:  |                      | :large_blue_diamond:  | :large_blue_diamond: |                      | :large_blue_diamond: |                    |
| apparmor_file_mprotect             | :large_blue_diamond:  |                      | :large_blue_diamond:  | :large_blue_diamond: |                      | :large_blue_diamond: |                    |
| apparmor_file_lock                 | :large_blue_diamond:  |                      | :large_blue_diamond:  |                      |                      | :large_blue_diamond: |                    |
| apparmor_ptrace_access_check       |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| apparmor_ptrace_traceme            |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| apparmor_capable                   |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| apparmor_task_setrlimit            |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| ------                             |                       |                      |                       |                      |                      |                      |                    |
| **_SELINUX_**                      |                       |                      |                       |                      |                      |                      |                    |
| selinux_ptrace_access_check        |                       |                      |                       |                      | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_ptrace_traceme             |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_capget                     |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_capset                     |     :red_circle:      |                      |     :red_circle:      |                      |                      |                      |                    |
| selinux_capable                    |     :red_circle:      |                      |                       |                      |                      | :large_blue_diamond: |                    |
| selinux_quotactl                   |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_quota_on                   |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_syslog                     |                       |                      |                       |                      | :large_blue_diamond: |                      |                    |
| selinux_vm_enough_memory           |     :red_circle:      |                      |                       |                      |     :red_circle:     |     :red_circle:     |                    |
| selinux_netlink_send               |                       |                      | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_sb_kern_mount              |     :red_circle:      |                      |     :red_circle:      |                      |     :red_circle:     |     :red_circle:     |                    |
| selinux_sb_statfs                  |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_mount                      |                       |                      | :large_blue_diamond:  |                      | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_umount                     |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_set_mnt_opts               |     :red_circle:      |                      |     :red_circle:      |                      |     :red_circle:     |     :red_circle:     |                    |
| selinux_inode_create               |     :red_circle:      |                      |                       |                      |                      |                      |                    |
| selinux_inode_link                 |                       |                      |                       |                      |                      | :large_blue_diamond: |                    |
| selinux_inode_unlink               |                       |                      |                       |                      |                      | :large_blue_diamond: |                    |
| selinux_inode_symlink              |     :red_circle:      |                      |                       |                      |                      |                      |                    |
| selinux_inode_mkdir                |     :red_circle:      |                      |                       |                      |                      |                      |                    |
| selinux_inode_rmdir                |                       |                      |                       |                      |                      | :large_blue_diamond: |                    |
| selinux_inode_mknod                |     :red_circle:      |                      |                       |                      |                      |                      |                    |
| selinux_inode_rename               |                       |                      |                       |     :red_circle:     |                      |                      |                    |
| selinux_inode_readlink             |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_inode_follow_link          |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_inode_permission           |                       |                      | :large_blue_diamond:  | :large_blue_diamond: |     :red_circle:     |     :red_circle:     |                    |
| selinux_inode_setattr              |                       |                      | :large_blue_diamond:  |                      | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_inode_getattr              |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_inode_setxattr             |                       |                      | :large_blue_diamond:  |                      |     :red_circle:     |     :red_circle:     |                    |
| selinux_inode_getxattr             |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_inode_listxattr            |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_inode_removexattr          |                       |                      | :large_blue_diamond:  |                      |     :red_circle:     | :large_blue_diamond: |                    |
| selinux_inode_getsecurity          |     :red_circle:      |                      |                       |                      |                      | :large_blue_diamond: |                    |
| selinux_file_permission            | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_file_ioctl                 |     :red_circle:      |                      | :large_blue_diamond:  |                      | :large_blue_diamond: |     :red_circle:     |                    |
| selinux_mmap_file                  |     :red_circle:      |                      | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_mmap_addr                  |                       |                      |                       |                      | :large_blue_diamond: |                      |                    |
| selinux_file_mprotect              |     :red_circle:      |                      | :large_blue_diamond:  | :large_blue_diamond: |     :red_circle:     |     :red_circle:     |                    |
| selinux_file_lock                  | :large_blue_diamond:  |                      | :large_blue_diamond:  |                      | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_file_fcntl                 | :large_blue_diamond:  |                      | :large_blue_diamond:  |                      | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_file_send_sigiotask        |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_file_receive               | :large_blue_diamond:  |                      | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_file_open                  |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_task_create                |     :red_circle:      |                      |     :red_circle:      |                      |                      |                      |                    |
| selinux_kernel_act_as              |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_kernel_create_files_as     |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_kernel_module_request      |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_task_setpgid               |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_task_getpgid               |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_task_getsid                |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_task_setnice               |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_task_setioprio             |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_task_getioprio             |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_task_setrlimit             |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_task_setscheduler          |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_task_getscheduler          |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_task_movememory            |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_task_kill                  | :large_blue_diamond:  |                      |                       |                      |                      |                      |                    |
| selinux_task_wait                  |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_ipc_permission             |                       |                      |                       |                      | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_msg_queue_alloc_security   |     :red_circle:      |                      |                       |                      |                      |     :red_circle:     |                    |
| selinux_msg_queue_associate        |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_msg_queue_msgctl           |                       |                      |                       |                      | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_msg_queue_msgsnd           |                       |                      |     :red_circle:      |                      |                      |                      |                    |
| selinux_msg_queue_msgrcv           |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_shm_alloc_security         |     :red_circle:      |                      |                       |                      |                      |     :red_circle:     |                    |
| selinux_shm_associate              |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_shm_shmctl                 |                       |                      |                       |                      | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_shm_shmat                  |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_sem_alloc_security         |     :red_circle:      |                      |                       |                      |                      |     :red_circle:     |                    |
| selinux_sem_associate              |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_sem_semctl                 |                       |                      |                       |                      | :large_blue_diamond: | :large_blue_diamond: |                    |
| selinux_sem_semop                  |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_getprocattr                | :large_blue_diamond:  |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_setprocattr                |                       |                      |     :red_circle:      |                      |     :red_circle:     |     :red_circle:     |                    |
| selinux_inode_getsecctx            |     :red_circle:      |                      |                       |                      |                      | :large_blue_diamond: |                    |
| selinux_socket_unix_stream_connect |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_socket_unix_may_send       |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_socket_create              |     :red_circle:      |                      |                       |                      |                      |                      |                    |
| selinux_socket_bind                |                       |                      |     :red_circle:      | :large_blue_diamond: |     :red_circle:     | :large_blue_diamond: |                    |
| selinux_socket_connect             |                       |                      |     :red_circle:      |     :red_circle:     |     :red_circle:     | :large_blue_diamond: |                    |
| selinux_socket_listen              |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_socket_accept              |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_socket_sendmsg             |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_socket_recvmsg             |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_socket_getsockname         |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_socket_getpeername         |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_socket_getsockopt          |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_socket_setsockopt          |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_socket_shutdown            |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_socket_sock_rcv_skb        | :large_blue_diamond:  |                      | :large_blue_diamond:  |                      |     :red_circle:     | :large_blue_diamond: |                    |
| selinux_secmark_relabel_packet     |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_tun_dev_create             |     :red_circle:      |                      |                       |                      |                      |                      |                    |
| selinux_tun_dev_attach_queue       |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_tun_dev_open               |     :red_circle:      |                      |                       |                      |                      |                      |                    |
| selinux_xfrm_policy_alloc          |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_xfrm_policy_delete         |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_xfrm_state_alloc           |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_xfrm_state_delete          |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_xfrm_policy_lookup         |                       |                      |                       |                      |                      |                      | :white_check_mark: |
| selinux_xfrm_state_pol_flow_match  |                       |                      | :large_blue_diamond:  |                      |                      |                      |                    |
| selinux_key_permission             |                       |                      |                       |                      | :large_blue_diamond: | :large_blue_diamond: |                    |
| ------                             |                       |                      |                       |                      |                      |                      |                    |

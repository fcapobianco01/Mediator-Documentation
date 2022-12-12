 : Explicit flows detected

 : Implicit flows detected

| Function                           | sub :arrow_right: obj  |  sub :arrow_right:op   | obj :arrow_right: sub  |  obj :arrow_right: op  |  op:arrow_right: sub   |  op :arrow_right: obj  |  No cross-domain   |
| ---------------------------------- | :--------------------: | :--------------------: | :--------------------: | :--------------------: | :--------------------: | :--------------------: | :----------------: |
| **_TOMOYO_**                       |                        |                        |                        |                        |                        |                        |                    |
| tomoyo_bprm_check_security         | :large_blue_diamond:*1 | :large_blue_diamond:*1 |                        |                        |                        |                        |                    |
| tomoyo_file_fcntl                  |                        |                        | :large_blue_diamond:*1 | :large_blue_diamond:*1 | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                    |
| tomoyo_file_ioctl                  |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| tomoyo_file_open                   |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| tomoyo_path_truncate               |                        |                        |                        |                        |                        | :large_blue_diamond:*1 |                    |
| tomoyo_path_unlink                 |                        |                        |                        |                        |                        | :large_blue_diamond:*1 |                    |
| tomoyo_path_mkdir                  |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| tomoyo_path_rmdir                  |                        |                        |                        |                        |                        | :large_blue_diamond:*1 |                    |
| tomoyo_path_symlink                |                        |                        |                        |                        |                        | :large_blue_diamond:*1 |                    |
| tomoyo_path_mknod                  |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| tomoyo_path_link                   |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| tomoyo_path_rename                 |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| tomoyo_inode_getattr               | :large_blue_diamond:*1 | :large_blue_diamond:*1 |                        |                        |                        | :large_blue_diamond:*1 |                    |
| tomoyo_path_chmod                  |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| tomoyo_path_chown                  | :large_blue_diamond:*1 | :large_blue_diamond:*1 | :large_blue_diamond:*1 | :large_blue_diamond:*1 | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                    |
| tomoyo_path_chroot                 |                        |                        |                        |                        |                        | :large_blue_diamond:*1 |                    |
| tomoyo_sb_mount                    |                        |                        |                        |                        |                        | :large_blue_diamond:*1 |                    |
| tomoyo_sb_umount                   |                        |                        |                        |                        |                        | :large_blue_diamond:*1 |                    |
| tomoyo_sb_pivotroot                |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| tomoyo_socket_bind                 |                        |                        | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                        | :large_blue_diamond:*1 |                    |
| tomoyo_socket_connect              |                        |                        | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                        | :large_blue_diamond:*1 |                    |
| tomoyo_socket_listen               |                        |                        | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                        | :large_blue_diamond:*1 |                    |
| tomoyo_socket_sendmsg              |                        |                        | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                        | :large_blue_diamond:*1 |                    |
| ------                             |                        |                        |                        |                        |                        |                        |                    |
| **_APPARMOR_**                     |                        |                        |                        |                        |                        |                        |                    |
| apparmor_path_link                 |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| apparmor_path_unlink               |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| apparmor_path_rmdir                |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| apparmor_path_symlink              |                        |                        |     :red_circle:*2     |                        |                        |                        |                    |
| apparmor_path_mkdir                |                        |                        |     :red_circle:*2     |                        |                        |                        |                    |
| apparmor_path_mknod                |                        |                        |     :red_circle:*2     |                        |                        |                        |                    |
| apparmor_path_rename               |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| apparmor_path_chmod                |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| apparmor_path_chown                |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| apparmor_path_truncate             |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| apparmor_inode_getattr             |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| apparmor_file_open                 |                        |                        |                        |                        |                        |     :red_circle:*1     |                    |
| apparmor_file_permission           | :large_blue_diamond:*2 |                        |                        |                        |                        |                        |                    |
| apparmor_mmap_file                 | :large_blue_diamond:*2 |                        |                        |                        |                        |                        |                    |
| apparmor_file_mprotect             | :large_blue_diamond:*2 |                        |                        | :large_blue_diamond:*1 |                        |                        |                    |
| apparmor_file_lock                 | :large_blue_diamond:*2 |                        |                        |                        |                        |                        |                    |
| apparmor_ptrace_access_check       |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| apparmor_ptrace_traceme            |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| apparmor_capable                   |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| apparmor_task_setrlimit            |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| ------                             |                        |                        |                        |                        |                        |                        |                    |
| **_SELINUX_**                      |                        |                        |                        |                        |                        |                        |                    |
| selinux_ptrace_access_check        |                        |                        |                        |                        | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                    |
| selinux_ptrace_traceme             |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_capget                     |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_capset                     |     :red_circle:*1     |                        |     :red_circle:*1     |                        |                        |                        |                    |
| selinux_capable                    |     :red_circle:*1     |                        |                        |                        |                        | :large_blue_diamond:*2 |                    |
| selinux_quotactl                   |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_quota_on                   |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_syslog                     |                        |                        |                        |                        | :large_blue_diamond:*1 |                        |                    |
| selinux_vm_enough_memory           |     :red_circle:*2     |                        |                        |                        |     :red_circle:*1     |     :red_circle:*1     |                    |
| selinux_netlink_send               |                        |                        | :large_blue_diamond:*1 | :large_blue_diamond:*1 | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                    |
| selinux_sb_kern_mount              |     :red_circle:*2     |                        |     :red_circle:*1     |                        |     :red_circle:*1     |     :red_circle:*1     |                    |
| selinux_sb_statfs                  |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_mount                      |                        |                        |                        |                        | :large_blue_diamond:*1 | :large_blue_diamond:*1 |                    |
| selinux_umount                     |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_set_mnt_opts               |     :red_circle:*2     |                        |     :red_circle:*1     |                        |     :red_circle:*1     |     :red_circle:*1     |                    |
| selinux_inode_create               |     :red_circle:*1     |                        |                        |                        |                        |                        |                    |
| selinux_inode_link                 |                        |                        |                        |                        |                        | :large_blue_diamond:*1 |                    |
| selinux_inode_unlink               |                        |                        |                        |                        |                        | :large_blue_diamond:*1 |                    |
| selinux_inode_symlink              |     :red_circle:*1     |                        |                        |                        |                        |                        |                    |
| selinux_inode_mkdir                |     :red_circle:*1     |                        |                        |                        |                        |                        |                    |
| selinux_inode_rmdir                |                        |                        |                        |                        |                        | :large_blue_diamond:*1 |                    |
| selinux_inode_mknod                |     :red_circle:*1     |                        |                        |                        |                        |                        |                    |
| selinux_inode_rename               |                        |                        |                        |     :red_circle:*1     |                        |                        |                    |
| selinux_inode_readlink             |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_inode_follow_link          |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_inode_permission           |                        |                        | :large_blue_diamond:*1 | :large_blue_diamond:*1 |     :red_circle:*1     |     :red_circle:*1     |                    |
| selinux_inode_setattr              |                        |                        |                        |                        | :large_blue_diamond:*1 | :large_blue_diamond:*1 |                    |
| selinux_inode_getattr              |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_inode_setxattr             |                        |                        |                        |                        |     :red_circle:*1     |     :red_circle:*1     |                    |
| selinux_inode_getxattr             |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_inode_listxattr            |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_inode_removexattr          |                        |                        | :large_blue_diamond:*1 |                        |     :red_circle:*1     | :large_blue_diamond:*1 |                    |
| selinux_inode_getsecurity          |     :red_circle:*2     |                        |                        |                        |                        | :large_blue_diamond:*1 |                    |
| selinux_file_permission            | :large_blue_diamond:*2 | :large_blue_diamond:*2 | :large_blue_diamond:*1 | :large_blue_diamond:*1 | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                    |
| selinux_file_ioctl                 |     :red_circle:*2     |                        | :large_blue_diamond:*1 |                        | :large_blue_diamond:*1 |     :red_circle:*1     |                    |
| selinux_mmap_file                  |     :red_circle:*2     |                        | :large_blue_diamond:*1 | :large_blue_diamond:*1 | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                    |
| selinux_mmap_addr                  |                        |                        | :large_blue_diamond:*1 |                        | :large_blue_diamond:*1 |                        |                    |
| selinux_file_mprotect              |     :red_circle:*2     |                        | :large_blue_diamond:*1 | :large_blue_diamond:*1 |     :red_circle:*1     |     :red_circle:*1     |                    |
| selinux_file_lock                  | :large_blue_diamond:*2 |                        | :large_blue_diamond:*1 |                        | :large_blue_diamond:*1 | :large_blue_diamond:*1 |                    |
| selinux_file_fcntl                 | :large_blue_diamond:*2 |                        | :large_blue_diamond:*1 |                        | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                    |
| selinux_file_send_sigiotask        |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_file_receive               | :large_blue_diamond:*2 |                        | :large_blue_diamond:*1 | :large_blue_diamond:*1 | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                    |
| selinux_file_open                  |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_task_create                |     :red_circle:*1     |                        |     :red_circle:*1     |                        |                        |                        |                    |
| selinux_kernel_act_as              |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_kernel_create_files_as     |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_kernel_module_request      |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_task_setpgid               |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_task_getpgid               |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_task_getsid                |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_task_setnice               |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_task_setioprio             |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_task_getioprio             |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_task_setrlimit             |                        |                        | :large_blue_diamond:*1 |                        |                        |                        |                    |
| selinux_task_setscheduler          |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_task_getscheduler          |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_task_movememory            |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_task_kill                  | :large_blue_diamond:*1 |                        |                        |                        |                        |                        |                    |
| selinux_task_wait                  |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_ipc_permission             |                        |                        |                        |                        | :large_blue_diamond:*2 | :large_blue_diamond:*2 |                    |
| selinux_msg_queue_alloc_security   |     :red_circle:*1     |                        |                        |                        |                        |     :red_circle:*1     |                    |
| selinux_msg_queue_associate        |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_msg_queue_msgctl           |                        |                        |                        |                        | :large_blue_diamond:*1 | :large_blue_diamond:*1 |                    |
| selinux_msg_queue_msgsnd           |                        |                        |     :red_circle:*1     |                        |                        |                        |                    |
| selinux_msg_queue_msgrcv           |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_shm_alloc_security         |     :red_circle:*1     |                        |                        |                        |                        |     :red_circle:*1     |                    |
| selinux_shm_associate              |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_shm_shmctl                 |                        |                        |                        |                        | :large_blue_diamond:*1 | :large_blue_diamond:*1 |                    |
| selinux_shm_shmat                  |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_sem_alloc_security         |     :red_circle:*1     |                        |                        |                        |                        |     :red_circle:*1     |                    |
| selinux_sem_associate              |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_sem_semctl                 |                        |                        |                        |                        | :large_blue_diamond:*1 | :large_blue_diamond:*1 |                    |
| selinux_sem_semop                  |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_getprocattr                |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_setprocattr                |                        |                        |     :red_circle:*1     |                        |     :red_circle:*1     |     :red_circle:*1     |                    |
| selinux_inode_getsecctx            |     :red_circle:*2     |                        |                        |                        |                        | :large_blue_diamond:*1 |                    |
| selinux_socket_unix_stream_connect |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_socket_unix_may_send       |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_socket_create              |     :red_circle:*2     |                        |                        |                        |                        |                        |                    |
| selinux_socket_bind                |                        |                        |     :red_circle:*1     | :large_blue_diamond:*1 |     :red_circle:*1     | :large_blue_diamond:*1 |                    |
| selinux_socket_connect             |                        |                        |     :red_circle:*1     |     :red_circle:*1     |     :red_circle:*1     | :large_blue_diamond:*1 |                    |
| selinux_socket_listen              |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_socket_accept              |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_socket_sendmsg             |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_socket_recvmsg             |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_socket_getsockname         |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_socket_getpeername         |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_socket_getsockopt          |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_socket_setsockopt          |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_socket_shutdown            |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_socket_sock_rcv_skb        | :large_blue_diamond:*1 |                        | :large_blue_diamond:*1 |                        |     :red_circle:*1     | :large_blue_diamond:*1 |                    |
| selinux_secmark_relabel_packet     |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_tun_dev_create             |     :red_circle:*1     |                        |                        |                        |                        |                        |                    |
| selinux_tun_dev_attach_queue       |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_tun_dev_open               |     :red_circle:*1     |                        |                        |                        |                        |                        |                    |
| selinux_xfrm_policy_alloc          |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_xfrm_policy_delete         |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_xfrm_state_alloc           |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_xfrm_state_delete          |                        |                        | :large_blue_diamond:*1 |                        |                        |                        |                    |
| selinux_xfrm_policy_lookup         |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| selinux_xfrm_state_pol_flow_match  |                        |                        | :large_blue_diamond:*1 |                        |                        |                        |                    |
| selinux_key_permission             |                        |                        |                        |                        |                        |                        | :white_check_mark: |
| ------                             |                        |                        |                        |                        |                        |                        |                    |
| **_X-SERVER_**                     |                        |                        |                        |                        |                        |                        |                    |
| dixLookupWindow                    |                        |                        |                        |                        |                        |                        |                    |
| dixLookupDrawable                  |                        |                        |                        |                        |                        |                        |                    |
| dixLookupClient                    |                        |                        |                        |                        |                        |                        |                    |
| dixLookupDevice                    |                        |                        |                        |                        |                        |                        |                    |
| dixLookupSelection                 |                        |                        |                        |                        |                        |                        |                    |
| dixLookupProperty                  |                        |                        |                        |                        |                        |                        |                    |
| ------                             |                        |                        |                        |                        |                        |                        |                    |

List of functions not being analyzed

| Funtion                          |             Reason             |
| -------------------------------- | :----------------------------: |
| **_TOMOYO_**                     |                                |
| tomoyo_cred_alloc_blank          |       Allocation or free       |
| tomoyo_cred_prepare              |         No clear sink          |
| tomoyo_cred_transfer             |         No clear sink          |
| tomoyo_cred_free                 |       Allocation or free       |
| tomoyo_bprm_set_creds            |         No clear sink          |
| ------                           |                                |
| **_APPARMOR_**                   |                                |
| apparmor_capget                  |         No clear sink          |
| apparmor_file_alloc_security     |         No clear sink          |
| apparmor_file_free_security      |         No clear sink          |
| apparmor_getprocattr             |         No clear sink          |
| apparmor_setprocattr             |         No clear sink          |
| apparmor_cred_alloc_blank        |         No clear sink          |
| apparmor_cred_free               |         No clear sink          |
| apparmor_cred_prepare            |         No clear sink          |
| apparmor_cred_transfer           |         No clear sink          |
| apparmor_bprm_set_creds          |         No clear sink          |
| apparmor_bprm_committing_creds   |         No clear sink          |
| apparmor_bprm_committed_creds    |         No clear sink          |
| apparmor_bprm_secureexec         |         No clear sink          |
| ------                           |                                |
| **_SELINUX_**                    |                                |
| selinux_bprm_set_creds           | No clear subject/object (bprm) |
| selinux_bprm_committing_creds    | No clear subject/object (bprm) |
| selinux_bprm_committed_creds     | No clear subject/object (bprm) |
| selinux_bprm_secureexec          | No clear subject/object (bprm) |
| selinux_sb_alloc_security        |       Allocation or free       |
| selinux_sb_free_security         |       Allocation or free       |
| selinux_sb_copy_data             |         No clear sink          |
| selinux_sb_remount               |         No clear sink          |
| selinux_sb_show_options          |         No clear sink          |
| selinux_sb_clone_mnt_opts        |         No clear sink          |
| selinux_parse_opts_str           |         No clear sink          |
| selinux_dentry_init_security     |         No clear sink          |
| selinux_inode_alloc_security     |       Allocation or free       |
| selinux_inode_free_security      |       Allocation or free       |
| selinux_inode_init_security      |         No clear sink          |
| selinux_inode_post_setxattr      |         No clear sink          |
| selinux_inode_setsecurity        |         No clear sink          |
| selinux_inode_listsecurity       |         No clear sink          |
| selinux_inode_getsecid           |         No clear sink          |
| selinux_file_alloc_security      |       Allocation or free       |
| selinux_file_free_security       |       Allocation or free       |
| selinux_file_set_fowner          |         No clear sink          |
| selinux_cred_alloc_blank         |         No clear sink          |
| selinux_cred_free                |         No clear sink          |
| selinux_cred_prepare             |         No clear sink          |
| selinux_cred_transfer            |         No clear sink          |
| selinux_task_getsecid            |         No clear sink          |
| selinux_task_to_inode            |         No clear sink          |
| selinux_ipc_getsecid             |         No clear sink          |
| selinux_msg_msg_alloc_security   |         No clear sink          |
| selinux_msg_msg_free_security    |         No clear sink          |
| selinux_msg_queue_free_security  |         No clear sink          |
| selinux_shm_free_security        |         No clear sink          |
| selinux_sem_free_security        |         No clear sink          |
| selinux_d_instantiate            |         No clear sink          |
| selinux_ismaclabel               |         No clear sink          |
| selinux_secid_to_secctx          |         No clear sink          |
| selinux_secctx_to_secid          |         No clear sink          |
| selinux_release_secctx           |         No clear sink          |
| selinux_inode_notifysecctx       |         No clear sink          |
| selinux_inode_setsecctx          |         No clear sink          |
| selinux_socket_post_create       |         No clear sink          |
| selinux_socket_getpeersec_stream |         No clear sink          |
| selinux_socket_getpeersec_dgram  |         No clear sink          |
| selinux_sk_alloc_security        |         No clear sink          |
| selinux_sk_free_security         |         No clear sink          |
| selinux_sk_clone_security        |         No clear sink          |
| selinux_sk_getsecid              |         No clear sink          |
| selinux_sock_graft               |         No clear sink          |
| selinux_inet_conn_request        |         No clear sink          |
| selinux_inet_csk_clone           |         No clear sink          |
| selinux_inet_conn_established    |         No clear sink          |
| selinux_secmark_refcount_inc     |         No clear sink          |
| selinux_secmark_refcount_dec     |         No clear sink          |
| selinux_req_classify_flow        |         No clear sink          |
| selinux_tun_dev_alloc_security   |         No clear sink          |
| selinux_tun_dev_free_security    |         No clear sink          |
| selinux_tun_dev_attach           |         No clear sink          |
| selinux_skb_owned_by             |         No clear sink          |
| selinux_xfrm_policy_clone        |                                |
| selinux_xfrm_policy_free         |                                |
| selinux_xfrm_state_free          |                                |
| selinux_xfrm_decode_session      |                                |
| selinux_key_alloc                |       Allocation or free       |
| selinux_key_free                 |       Allocation or free       |
| selinux_key_getsecurity          |       Allocation or free       |
| selinux_audit_rule_init          |         No clear sink          |
| selinux_audit_rule_known         |         No clear sink          |
| selinux_audit_rule_match         |         No clear sink          |
| selinux_audit_rule_free          |       Allocation or free       |
| ------                           |                                |
| **_X-SERVER_**                   |                                |
| dixLookupPrivate                 |         No clear sink          |
| dixLookupScreenPrivate           |         No clear sink          |
| ------                           |                                |

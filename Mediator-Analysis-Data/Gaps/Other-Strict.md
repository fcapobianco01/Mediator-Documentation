 : Explicit flows detected

 : Implicit flows detected

| Function                           | dynamic :arrow_right: static | input :arrow_right: mediator | external :arrow_right: input | external :arrow_right: mediator |  No location/type  |
| ---------------------------------- | :--------------------------: | :--------------------------: | :--------------------------: | :-----------------------------: | :----------------: |
| **_TOMOYO_**                       |                              |                              |                              |                                 |                    |
| tomoyo_bprm_check_security         |                              |     :large_blue_diamond:     |         :red_circle:         |                                 |                    |
| tomoyo_file_fcntl                  |         :red_circle:         |         :red_circle:         |         :red_circle:         |          :red_circle:           |                    |
| tomoyo_file_ioctl                  |         :red_circle:         |         :red_circle:         |         :red_circle:         |                                 |                    |
| tomoyo_file_open                   |         :red_circle:         |         :red_circle:         |         :red_circle:         |                                 |                    |
| tomoyo_path_truncate               |                              |     :large_blue_diamond:     |         :red_circle:         |                                 |                    |
| tomoyo_path_unlink                 |                              |     :large_blue_diamond:     |         :red_circle:         |                                 |                    |
| tomoyo_path_mkdir                  |         :red_circle:         |         :red_circle:         |         :red_circle:         |          :red_circle:           |                    |
| tomoyo_path_rmdir                  |                              |     :large_blue_diamond:     |         :red_circle:         |                                 |                    |
| tomoyo_path_symlink                |                              |     :large_blue_diamond:     |         :red_circle:         |                                 |                    |
| tomoyo_path_mknod                  |         :red_circle:         |         :red_circle:         |         :red_circle:         |                                 |                    |
| tomoyo_path_link                   |                              |                              |         :red_circle:         |                                 |                    |
| tomoyo_path_rename                 |                              |                              |         :red_circle:         |                                 |                    |
| tomoyo_inode_getattr               |                              |     :large_blue_diamond:     |         :red_circle:         |                                 |                    |
| tomoyo_path_chmod                  |         :red_circle:         |         :red_circle:         |         :red_circle:         |          :red_circle:           |                    |
| tomoyo_path_chown                  |                              |         :red_circle:         |         :red_circle:         |      :large_blue_diamond:       |                    |
| tomoyo_path_chroot                 |                              |     :large_blue_diamond:     |         :red_circle:         |                                 |                    |
| tomoyo_sb_mount                    |         :red_circle:         |     :large_blue_diamond:     |                              |          :red_circle:           |                    |
| tomoyo_sb_umount                   |                              |     :large_blue_diamond:     |         :red_circle:         |                                 |                    |
| tomoyo_sb_pivotroot                |                              |                              |         :red_circle:         |                                 |                    |
| tomoyo_socket_bind                 |         :red_circle:         |         :red_circle:         |         :red_circle:         |                                 |                    |
| tomoyo_socket_connect              |         :red_circle:         |         :red_circle:         |         :red_circle:         |                                 |                    |
| tomoyo_socket_listen               |         :red_circle:         |         :red_circle:         |         :red_circle:         |                                 |                    |
| tomoyo_socket_sendmsg              |         :red_circle:         |         :red_circle:         |         :red_circle:         |                                 |                    |
| ------                             |                              |                              |                              |                                 |                    |
| **_APPARMOR_**                     |                              |                              |                              |                                 |                    |
| apparmor_path_link                 |                              |         :red_circle:         |                              |                                 |                    |
| apparmor_path_unlink               |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| apparmor_path_symlink              |                              |         :red_circle:         |         :red_circle:         |          :red_circle:           |                    |
| apparmor_path_mkdir                |                              |         :red_circle:         |         :red_circle:         |          :red_circle:           |                    |
| apparmor_path_rmdir                |                              |         :red_circle:         |         :red_circle:         |      :large_blue_diamond:       |                    |
| apparmor_path_mknod                |                              |         :red_circle:         |         :red_circle:         |          :red_circle:           |                    |
| apparmor_path_rename               |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| apparmor_path_chmod                |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| apparmor_path_chown                |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| apparmor_path_truncate             |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| apparmor_inode_getattr             |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| apparmor_file_open                 |     :large_blue_diamond:     |     :large_blue_diamond:     |                              |          :red_circle:           |                    |
| apparmor_file_permission           |         :red_circle:         |         :red_circle:         |         :red_circle:         |                                 |                    |
| apparmor_mmap_file                 |     :large_blue_diamond:     |         :red_circle:         |         :red_circle:         |          :red_circle:           |                    |
| apparmor_file_mprotect             |     :large_blue_diamond:     |         :red_circle:         |         :red_circle:         |      :large_blue_diamond:       |                    |
| apparmor_file_lock                 |     :large_blue_diamond:     |         :red_circle:         |         :red_circle:         |          :red_circle:           |                    |
| apparmor_ptrace_access_check       |         :red_circle:         |         :red_circle:         |         :red_circle:         |                                 |                    |
| apparmor_ptrace_traceme            |                              |                              |                              |          :red_circle:           |                    |
| apparmor_capable                   |                              |                              |                              |                                 | :white_check_mark: |
| apparmor_task_setrlimit            |                              |                              |         :red_circle:         |                                 |                    |
| ------                             |                              |                              |                              |                                 |                    |
| **_SELINUX_**                      |                              |                              |                              |                                 |                    |
| selinux_ptrace_access_check        |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_ptrace_traceme             |                              |                              |                              |          :red_circle:           |                    |
| selinux_capget                     |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_capset                     |                              |         :red_circle:         |                              |                                 |                    |
| selinux_capable                    |         :red_circle:         |         :red_circle:         |                              |          :red_circle:           |                    |
| selinux_quotactl                   |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_quota_on                   |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_syslog                     |                              |                              |         :red_circle:         |                                 |                    |
| selinux_vm_enough_memory           |                              |                              |         :red_circle:         |          :red_circle:           |                    |
| selinux_netlink_send               |         :red_circle:         |         :red_circle:         |         :red_circle:         |      :large_blue_diamond:       |                    |
| selinux_sb_kern_mount              |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_sb_statfs                  |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_mount                      |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_umount                     |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_set_mnt_opts               |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_create               |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_link                 |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_unlink               |         :red_circle:         |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_symlink              |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_mkdir                |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_rmdir                |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_mknod                |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_rename               |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_readlink             |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_follow_link          |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_permission           |     :large_blue_diamond:     |         :red_circle:         |         :red_circle:         |      :large_blue_diamond:       |                    |
| selinux_inode_setattr              |     :large_blue_diamond:     |         :red_circle:         |         :red_circle:         |      :large_blue_diamond:       |                    |
| selinux_inode_getattr              |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_setxattr             |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_getxattr             |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_listxattr            |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_removexattr          |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_getsecurity          |                              |                              |         :red_circle:         |          :red_circle:           |                    |
| selinux_file_permission            |     :large_blue_diamond:     |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_file_ioctl                 |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_mmap_file                  |     :large_blue_diamond:     |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_mmap_addr                  |                              |                              |                              |                                 | :white_check_mark: |
| selinux_file_mprotect              |     :large_blue_diamond:     |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_file_lock                  |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_file_fcntl                 |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_file_send_sigiotask        |     :large_blue_diamond:     |         :red_circle:         |                              |                                 |                    |
| selinux_file_receive               |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_file_open                  |     :large_blue_diamond:     |         :red_circle:         |                              |                                 |                    |
| selinux_task_create                |                              |                              |         :red_circle:         |          :red_circle:           |                    |
| selinux_kernel_act_as              |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_kernel_create_files_as     |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_kernel_module_request      |                              |                              |         :red_circle:         |                                 |                    |
| selinux_task_setpgid               |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_task_getpgid               |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_task_getsid                |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_task_setnice               |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_task_setioprio             |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_task_getioprio             |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_task_setrlimit             |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_task_setscheduler          |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_task_getscheduler          |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_task_movememory            |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_task_kill                  |         :red_circle:         |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_task_wait                  |                              |                              |                              |          :red_circle:           |                    |
| selinux_ipc_permission             |     :large_blue_diamond:     |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_msg_queue_alloc_security   |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_msg_queue_associate        |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_msg_queue_msgctl           |     :large_blue_diamond:     |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_msg_queue_msgsnd           |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_msg_queue_msgrcv           |                              |         :red_circle:         |                              |                                 |                    |
| selinux_shm_alloc_security         |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_shm_associate              |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_shm_shmctl                 |         :red_circle:         |         :red_circle:         |         :red_circle:         |          :red_circle:           |                    |
| selinux_shm_shmat                  |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_sem_alloc_security         |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_sem_associate              |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_sem_semctl                 |         :red_circle:         |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_sem_semop                  |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_getprocattr                |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_setprocattr                |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_inode_getsecctx            |                              |                              |         :red_circle:         |          :red_circle:           |                    |
| selinux_socket_unix_stream_connect |                              |         :red_circle:         |                              |                                 |                    |
| selinux_socket_unix_may_send       |                              |         :red_circle:         |                              |                                 |                    |
| selinux_socket_create              |                              |                              |         :red_circle:         |                                 |                    |
| selinux_socket_bind                |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_socket_connect             |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_socket_listen              |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_socket_accept              |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_socket_sendmsg             |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_socket_recvmsg             |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_socket_getsockname         |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_socket_getpeername         |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_socket_getsockopt          |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_socket_setsockopt          |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_socket_shutdown            |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_socket_sock_rcv_skb        |                              |         :red_circle:         |                              |                                 |                    |
| selinux_secmark_relabel_packet     |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_tun_dev_create             |                              |                              |         :red_circle:         |                                 |                    |
| selinux_tun_dev_attach_queue       |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_tun_dev_open               |                              |         :red_circle:         |         :red_circle:         |                                 |                    |
| selinux_xfrm_policy_alloc          |                              |         :red_circle:         |                              |                                 |                    |
| selinux_xfrm_policy_delete         |                              |         :red_circle:         |                              |                                 |                    |
| selinux_xfrm_state_alloc           |                              |         :red_circle:         |                              |                                 |                    |
| selinux_xfrm_state_delete          |                              |         :red_circle:         |                              |                                 |                    |
| selinux_xfrm_policy_lookup         |                              |         :red_circle:         |                              |                                 |                    |
| selinux_xfrm_state_pol_flow_match  |                              |         :red_circle:         |                              |                                 |                    |
| selinux_key_permission             |         :red_circle:         |         :red_circle:         |                              |                                 |                    |
| ------                             |                              |                              |                              |                                 |                    |

List of functions not being analyzed

| Function                         |             Reason             |
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
| selinux_xfrm_state_alloc_acquire |                                |
| selinux_xfrm_state_free          |                                |
| selinux_xfrm_decode_session      |                                |
| selinux_key_alloc                |       Allocation or free       |
| selinux_key_free                 |       Allocation or free       |
| selinux_key_getsecurity          |       Allocation or free       |
| selinux_audit_rule_init          |         No clear sink          |
| selinux_audit_rule_known         |         No clear sink          |
| selinux_audit_rule_match         |         No clear sink          |
| selinux_audit_rule_free          |       Allocation or free       |

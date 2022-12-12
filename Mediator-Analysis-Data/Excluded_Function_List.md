
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
| selinux_xfrm_state_free          |                                |
| selinux_xfrm_decode_session      |                                |
| selinux_key_alloc                |       Allocation or free       |
| selinux_key_free                 |       Allocation or free       |
| selinux_key_getsecurity          |       Allocation or free       |
| selinux_audit_rule_init          |         No clear sink          |
| selinux_audit_rule_known         |         No clear sink          |
| selinux_audit_rule_match         |         No clear sink          |
| selinux_audit_rule_free          |       Allocation or free       |

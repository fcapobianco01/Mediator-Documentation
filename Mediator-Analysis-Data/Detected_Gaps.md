:red_circle: : Explicit flows detected

:large_blue_diamond: : Implicit flows detected

| Funtion                      | sub :arrow_right: obj | sub :arrow_right:op  | obj :arrow_right: sub |       obj :arrow_right: op        | op:arrow_right: sub  |       op :arrow_right: obj        |  No cross-domain   |
| ---------------------------- | :-------------------: | :------------------: | :-------------------: | :-------------------------------: | :------------------: | :-------------------------------: | :----------------: |
| **_TOMOYO_**                 |                       |                      |                       |                                   |                      |                                   |                    |
| tomoyo_bprm_check_security   | :large_blue_diamond:  | :large_blue_diamond: |                       |       :large_blue_diamond:        |                      |       :large_blue_diamond:        |                    |
| tomoyo_file_fcntl            | :large_blue_diamond:  | :large_blue_diamond: |                       |       :large_blue_diamond:        |                      |       :large_blue_diamond:        |                    |
| tomoyo_file_ioctl            |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |                    |
| tomoyo_file_open             | :large_blue_diamond:  | :large_blue_diamond: |                       |       :large_blue_diamond:        |                      |       :large_blue_diamond:        |                    |
| tomoyo_path_truncate         | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |                    |
| tomoyo_path_unlink           | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |                    |
| tomoyo_path_mkdir            |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |                    |
| tomoyo_path_rmdir            | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |                    |
| tomoyo_path_symlink          | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |                    |
| tomoyo_path_mknod            | :large_blue_diamond:  | :large_blue_diamond: |                       |       :large_blue_diamond:        |                      |                                   |                    |
| tomoyo_path_link             |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |                    |
| tomoyo_path_rename           |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |                    |
| tomoyo_inode_getattr         | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |                    |
| tomoyo_path_chmod            |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |                    |
| tomoyo_path_chown            |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |                    |
| tomoyo_path_chroot           | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |                    |
| tomoyo_sb_mount              |                       | :large_blue_diamond: |                       | :red_circle: :large_blue_diamond: |                      | :red_circle: :large_blue_diamond: |                    |
| tomoyo_sb_umount             | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |                    |
| tomoyo_sb_pivotroot          |                       |                      |                       | :red_circle: :large_blue_diamond: |                      |                                   |                    |
| tomoyo_socket_bind           | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :red_circle: :large_blue_diamond: | :large_blue_diamond: |       :large_blue_diamond:        |                    |
| tomoyo_socket_connect        | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :red_circle: :large_blue_diamond: | :large_blue_diamond: |       :large_blue_diamond:        |                    |
| tomoyo_socket_listen         | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :red_circle: :large_blue_diamond: | :large_blue_diamond: |       :large_blue_diamond:        |                    |
| tomoyo_socket_sendmsg        | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :red_circle: :large_blue_diamond: | :large_blue_diamond: |       :large_blue_diamond:        |                    |
| ------                       |                       |                      |                       |                                   |                      |                                   |                    |
| **_APPARMOR_**               |                       |                      |                       |                                   |                      |                                   |                    |
| apparmor_path_link           | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_path_unlink         | :large_blue_diamond:  |                      |                       |                                   | :large_blue_diamond: |       :large_blue_diamond:        |                    |
| apparmor_path_symlink        | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_path_mkdir          | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_path_rmdir          | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_path_mknod          | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_path_rename         | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_path_chmod          | :large_blue_diamond:  |                      |                       |                                   |                      |       :large_blue_diamond:        |                    |
| apparmor_path_chown          | :large_blue_diamond:  |                      |                       |                                   |                      |       :large_blue_diamond:        |                    |
| apparmor_path_truncate       | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_inode_getatt        | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_file_open           | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_file_permission     | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_mmap_file           |                       |                      |                       |                                   |                      |                                   |                    |
| cap_mmap_addr                |                       |                      |                       |                                   |                      |                                   |                    |
| apparmor_file_mprotect       |                       |                      |                       |                                   |                      |                                   |                    |
| apparmor_file_lock           | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_getprocattr         |                       |                      |                       |                                   |                      |                                   |                    |
| apparmor_setprocattr         |                       |                      |                       |                                   |                      |                                   |                    |
| apparmor_ptrace_access_check | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_ptrace_traceme      | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_capget              | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_capable             | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| apparmor_task_setrlimit      | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |                    |
| ------                       |                       |                      |                       |                                   |                      |                                   |                    |
| **_SELINUX_**                |                       |                      |                       |                                   |                      |                                   |                    |
| selinux_ptrace_access_check  |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_ptrace_traceme       |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_capget               |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_capset               |     :red_circle:      |                      |     :red_circle:      |                                   |                      |                                   |                    |
| selinux_capable              |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_quotactl             |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_quota_on             |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_syslog               |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_vm_enough_memory     |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_netlink_send         |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |                    |
| selinux_sb_kern_mount        |     :red_circle:      |                      |     :red_circle:      |                                   |                      |                                   |                    |
| selinux_sb_statfs            |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_mount                |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_umount               |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_set_mnt_opts         |     :red_circle:      |                      |     :red_circle:      |                                   |                      |                                   |                    |
| selinux_inode_create         |     :red_circle:      |                      | :large_blue_diamond:  |                                   |                      |                                   |                    |
| selinux_inode_link           |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_inode_unlink         |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_inode_symlink        |     :red_circle:      |                      | :large_blue_diamond:  |                                   |                      |                                   |                    |
| selinux_inode_mkdir          |     :red_circle:      |                      | :large_blue_diamond:  |                                   |                      |                                   |                    |
| selinux_inode_rmdir          |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_inode_mknod          |     :red_circle:      |                      | :large_blue_diamond:  |                                   |                      |                                   |                    |
| selinux_inode_rename         | :large_blue_diamond:  | :large_blue_diamond: |                       |           :red_circle:            |                      |                                   |                    |
| selinux_inode_readlink       |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_inode_follow_link    |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_inode_permission     |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |                    |
| selinux_inode_setattr        |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_inode_getattr        |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_inode_setxattr       | :large_blue_diamond:  |                      | :large_blue_diamond:  |                                   |                      |                                   |                    |
| selinux_inode_getxattr       |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_inode_listxattr      |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_inode_removexattr    |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_inode_getsecurity    |                       |                      |                       |                                   |                      |                                   | :white_check_mark: |
| selinux_file_open            |                       |                      |                       |       :large_blue_diamond:        |                      |           :red_circle:            |                    |
| ------                       |                       |                      |                       |                                   |                      |                                   |                    |
| **_X-SERVER_**               |                       |                      |                       |                                   |                      |                                   |                    |
| dixLookupWindow              |     :red_circle:      |                      |                       |                                   |                      |       :large_blue_diamond:        |                    |
| dixLookupDrawable            |     :red_circle:      |                      |                       |                                   |                      |       :large_blue_diamond:        |                    |
| dixLookupClient              |     :red_circle:      |                      |                       |                                   |                      |       :large_blue_diamond:        |                    |
| dixLookupDevice              |     :red_circle:      |                      |                       |                                   |                      |                                   |                    |
| dixLookupSelection           |     :red_circle:      |                      |                       |                                   |                      |                                   |                    |
| dixLookupProperty            |     :red_circle:      |                      |                       |                                   |                      |                                   |                    |
| ------                       |                       |                      |                       |                                   |                      |                                   |                    |

List of functions not being analyzed

| Funtion                        |             Reason             |
| ------------------------------ | :----------------------------: |
| **_TOMOYO_**                   |                                |
| tomoyo_cred_alloc_blank        |         No clear sink          |
| tomoyo_cred_prepare            |         No clear sink          |
| tomoyo_cred_transfer           |         No clear sink          |
| tomoyo_cred_free               |         No clear sink          |
| tomoyo_bprm_set_creds          |         No clear sink          |
| ------                         |                                |
| **_APPARMOR_**                 |                                |
| apparmor_file_alloc_security   |         No clear sink          |
| apparmor_file_free_security    |         No clear sink          |
| apparmor_cred_alloc_blank      |         No clear sink          |
| apparmor_cred_free             |         No clear sink          |
| apparmor_cred_prepare          |         No clear sink          |
| apparmor_cred_transfer         |         No clear sink          |
| apparmor_bprm_set_creds        |         No clear sink          |
| apparmor_bprm_committing_creds |         No clear sink          |
| apparmor_bprm_committed_creds  |         No clear sink          |
| apparmor_bprm_secureexec       |         No clear sink          |
| ------                         |                                |
| **_SELINUX_**                  |                                |
| selinux_bprm_set_creds         | No clear subject/object (bprm) |
| selinux_bprm_committing_creds  | No clear subject/object (bprm) |
| selinux_bprm_committed_creds   | No clear subject/object (bprm) |
| selinux_bprm_secureexec        | No clear subject/object (bprm) |
| selinux_sb_alloc_security      |       Allocation or free       |
| selinux_sb_free_security       |       Allocation or free       |
| selinux_sb_copy_data           |         No clear sink          |
| selinux_sb_remount             |         No clear sink          |
| selinux_sb_show_options        |         No clear sink          |
| selinux_sb_clone_mnt_opts      |         No clear sink          |
| selinux_parse_opts_str         |         No clear sink          |
| selinux_dentry_init_security   |         No clear sink          |
| selinux_inode_alloc_security   |       Allocation or free       |
| selinux_inode_free_security    |       Allocation or free       |
| selinux_inode_init_security    |         No clear sink          |
| selinux_inode_post_setxattr    |         No clear sink          |
| selinux_inode_setsecurity      |         No clear sink          |
| selinux_inode_listsecurity     |         No clear sink          |
| selinux_inode_getsecid         |         No clear sink          |
| selinux_key_alloc              |       Allocation or free       |
| selinux_key_free               |       Allocation or free       |
| selinux_audit_rule_init        |         No clear sink          |
| selinux_audit_rule_known       |         No clear sink          |
| selinux_audit_rule_match       |         No clear sink          |
| selinux_audit_rule_free        |       Allocation or free       |
| ------                         |                                |
| **_X-SERVER_**                 |                                |
| dixLookupPrivate               |         No clear sink          |
| dixLookupScreenPrivate         |         No clear sink          |
| ------                         |                                |

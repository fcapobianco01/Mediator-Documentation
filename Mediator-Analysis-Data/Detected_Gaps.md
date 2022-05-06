:red_circle: : Explicit flows detected

:large_blue_diamond: : Implicit flows detected

| Funtion                            | sub :arrow_right: obj | sub :arrow_right: op | obj :arrow_right: sub |       obj :arrow_right: op        | op :arrow_right: sub |       op :arrow_right: obj        |
| ---------------------------------- | :-------------------: | :------------------: | :-------------------: | :-------------------------------: | :------------------: | :-------------------------------: |
| **_TOMOYO_**                       |                       |                      |                       |                                   |                      |                                   |
| tomoyo_bprm_check_security         | :large_blue_diamond:  | :large_blue_diamond: |                       |       :large_blue_diamond:        |                      |       :large_blue_diamond:        |
| tomoyo_file_fcntl                  | :large_blue_diamond:  | :large_blue_diamond: |                       |       :large_blue_diamond:        |                      |       :large_blue_diamond:        |
| tomoyo_file_ioctl                  |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_file_open                   | :large_blue_diamond:  | :large_blue_diamond: |                       |       :large_blue_diamond:        |                      |       :large_blue_diamond:        |
| tomoyo_path_truncate               | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_path_unlink                 | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_path_mkdir                  |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_path_rmdir                  | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_path_symlink                | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_path_mknod                  | :large_blue_diamond:  | :large_blue_diamond: |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_path_link                   |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_path_rename                 |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_inode_getattr               | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_path_chmod                  |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_path_chown                  |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_path_chroot                 | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_sb_mount                    |                       | :large_blue_diamond: |                       | :red_circle: :large_blue_diamond: |                      | :red_circle: :large_blue_diamond: |
| tomoyo_sb_umount                   | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_sb_pivotroot                |                       |                      |                       | :red_circle: :large_blue_diamond: |                      |                                   |
| tomoyo_socket_bind                 | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :red_circle: :large_blue_diamond: | :large_blue_diamond: |       :large_blue_diamond:        |
| tomoyo_socket_connect              | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :red_circle: :large_blue_diamond: | :large_blue_diamond: |       :large_blue_diamond:        |
| tomoyo_socket_listen               | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :red_circle: :large_blue_diamond: | :large_blue_diamond: |       :large_blue_diamond:        |
| tomoyo_socket_sendmsg              | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :red_circle: :large_blue_diamond: | :large_blue_diamond: |       :large_blue_diamond:        |
| ------                             |                       |                      |                       |                                   |                      |                                   |
| **_APPARMOR_**                     |                       |                      |                       |                                   |                      |                                   |
| apparmor_path_link                 | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_path_unlink               | :large_blue_diamond:  |                      |                       |                                   | :large_blue_diamond: |       :large_blue_diamond:        |
| apparmor_path_symlink              | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_path_mkdir                | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_path_rmdir                | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_path_mknod                | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_path_rename               | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_path_chmod                | :large_blue_diamond:  |                      |                       |                                   |                      |       :large_blue_diamond:        |
| apparmor_path_chown                | :large_blue_diamond:  |                      |                       |                                   |                      |       :large_blue_diamond:        |
| apparmor_path_truncate             | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_inode_getatt              | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_file_open                 | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_file_permission           | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| ~~apparmor_file_alloc_security~~   |                       |                      |                       |                                   |                      |                                   |
| ~~apparmor_file_free_security~~    |                       |                      |                       |                                   |                      |                                   |
| apparmor_mmap_file                 |                       |                      |                       |                                   |                      |                                   |
| cap_mmap_addr                      |                       |                      |                       |                                   |                      |                                   |
| apparmor_file_mprotect             |                       |                      |                       |                                   |                      |                                   |
| apparmor_file_lock                 | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_getprocattr               |                       |                      |                       |                                   |                      |                                   |
| apparmor_setprocattr               |                       |                      |                       |                                   |                      |                                   |
| ~~apparmor_cred_alloc_blank~~      |                       |                      |                       |                                   |                      |                                   |
| ~~apparmor_cred_free~~             |                       |                      |                       |                                   |                      |                                   |
| ~~apparmor_cred_prepare~~          |                       |                      |                       |                                   |                      |                                   |
| ~~apparmor_cred_transfer~~         |                       |                      |                       |                                   |                      |                                   |
| ~~apparmor_bprm_set_creds~~        |                       |                      |                       |                                   |                      |                                   |
| ~~apparmor_bprm_committing_creds~~ |                       |                      |                       |                                   |                      |                                   |
| ~~apparmor_bprm_committed_creds~~  |                       |                      |                       |                                   |                      |                                   |
| ~~apparmor_bprm_secureexec~~       |                       |                      |                       |                                   |                      |                                   |
| apparmor_ptrace_access_check       | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_ptrace_traceme            | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_capget                    | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_capable                   | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| apparmor_task_setrlimit            | :large_blue_diamond:  |                      |                       |                                   |                      |                                   |
| ------                             |                       |                      |                       |                                   |                      |                                   |
| **_SELINUX_**                      |                       |                      |                       |                                   |                      |                                   |
| ------                             |                       |                      |                       |                                   |                      |                                   |
| **_X-SERVER_**                     |                       |                      |                       |                                   |                      |                                   |
| dixLookupWindow                    |     :red_circle:      |                      |                       |                                   |                      |       :large_blue_diamond:        |
| dixLookupDrawable                  |     :red_circle:      |                      |                       |                                   |                      |       :large_blue_diamond:        |
| dixLookupPrivate                   |                       |                      |                       |                                   |                      |                                   |
| dixLookupScreenPrivate             |                       |                      |                       |                                   |                      |                                   |
| dixLookupClient                    |     :red_circle:      |                      |                       |                                   |                      |       :large_blue_diamond:        |
| dixLookupDevice                    |     :red_circle:      |                      |                       |                                   |                      |                                   |
| dixLookupSelection                 |     :red_circle:      |                      |                       |                                   |                      |                                   |
| dixLookupProperty                  |     :red_circle:      |                      |                       |                                   |                      |                                   |
| ------                             |                       |                      |                       |                                   |                      |                                   |

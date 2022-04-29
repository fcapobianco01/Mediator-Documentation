:red_circle: : Explicit flows detected

:large_blue_diamond: : Implicit flows detected

| Funtion                    | sub :arrow_right: obj | sub :arrow_right: op | obj :arrow_right: sub |       obj :arrow_right: op        | op :arrow_right: sub |       op :arrow_right: obj        |
| -------------------------- | :-------------------: | :------------------: | :-------------------: | :-------------------------------: | :------------------: | :-------------------------------: |
| **_TOMOYO_**               |                       |                      |                       |                                   |                      |                                   |
| tomoyo_bprm_check_security | :large_blue_diamond:  | :large_blue_diamond: |                       |       :large_blue_diamond:        |                      |       :large_blue_diamond:        |
| tomoyo_file_fcntl          | :large_blue_diamond:  | :large_blue_diamond: |                       |       :large_blue_diamond:        |                      |       :large_blue_diamond:        |
| tomoyo_file_ioctl          |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_file_open           | :large_blue_diamond:  | :large_blue_diamond: |                       |       :large_blue_diamond:        |                      |       :large_blue_diamond:        |
| tomoyo_path_truncate       | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_path_unlink         | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_path_mkdir          |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_path_rmdir          | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_path_symlink        | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_path_mknod          | :large_blue_diamond:  | :large_blue_diamond: |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_path_link           |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_path_rename         |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_inode_getattr       | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_path_chmod          |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_path_chown          |                       |                      |                       |       :large_blue_diamond:        |                      |                                   |
| tomoyo_path_chroot         | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_sb_mount            |                       | :large_blue_diamond: |                       | :red_circle: :large_blue_diamond: |                      | :red_circle: :large_blue_diamond: |
| tomoyo_sb_umount           | :large_blue_diamond:  | :large_blue_diamond: |                       |                                   |                      |       :large_blue_diamond:        |
| tomoyo_sb_pivotroot        |                       |                      |                       | :red_circle: :large_blue_diamond: |                      |                                   |
| tomoyo_socket_bind         | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :red_circle: :large_blue_diamond: | :large_blue_diamond: |       :large_blue_diamond:        |
| tomoyo_socket_connect      | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :red_circle: :large_blue_diamond: | :large_blue_diamond: |       :large_blue_diamond:        |
| tomoyo_socket_listen       | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :red_circle: :large_blue_diamond: | :large_blue_diamond: |       :large_blue_diamond:        |
| tomoyo_socket_sendmsg      | :large_blue_diamond:  | :large_blue_diamond: | :large_blue_diamond:  | :red_circle: :large_blue_diamond: | :large_blue_diamond: |       :large_blue_diamond:        |
| ------                     |                       |                      |                       |                                   |                      |                                   |
| APPARMOR                   |                       |                      |                       |                                   |                      |                                   |
| ------                     |                       |                      |                       |                                   |                      |                                   |
| SELINUX                    |                       |                      |                       |                                   |                      |                                   |
| ------                     |                       |                      |                       |                                   |                      |                                   |
| X-SERVER                   |                       |                      |                       |                                   |                      |                                   |
| ------                     |                       |                      |                       |                                   |                      |                                   |

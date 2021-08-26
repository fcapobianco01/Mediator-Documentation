## **Tomoyo Hook Functions:**

#### Credentials
1. tomoyo_cred_alloc_blank  - *No Data*
2. tomoyo_cred_prepare  - *No Data*
3. tomoyo_cred_transfer  - *No Data*
4. tomoyo_cred_free  - *No Data*
   
#### Exec
5. tomoyo_bprm_set_creds
6. [tomoyo_bprm_check_security](Tomoyo/tomoyo_bprm_check_security.md) - *Not Verified*
   
#### Paths & Files
7. [tomoyo_file_fcntl](Tomoyo/tomoyo_file_fcntl.md) - *Not Verified*
8. [tomoyo_file_open](Tomoyo/tomoyo_file_open.md) - *Not Verified*
9. [tomoyo_path_truncate](Tomoyo/tomoyo_path_truncate.md) - *Not Verified* 
10. [tomoyo_path_unlink](Tomoyo/tomoyo_path_unlink.md) - *Not Verified*
11. [tomoyo_path_mkdir](Tomoyo/tomoyo_path_mkdir_data.md) - *Not Verified*
12. [tomoyo_path_rmdir](Tomoyo/tomoyo_path_rmdir.md) - *Not Verified*
13. [tomoyo_path_symlink](Tomoyo/tomoyo_path_symlink.md) - *Not Verified*
14. [tomoyo_path_mknod](Tomoyo/tomoyo_path_mknod.md) - *Not Verified*
15. [tomoyo_path_link](Tomoyo/tomoyo_path_link.md) - *Not Verified*
16. [tomoyo_path_rename](Tomoyo/tomoyo_path_rename.md) - *Not Verified*
17. [tomoyo_inode_getattr](Tomoyo/tomoyo_inode_getattr.md) - *Not Verified*
18. [tomoyo_file_ioctl](Tomoyo/tomoyo_file_ioctl.md) - *Not Verified*
19. [tomoyo_path_chmod](Tomoyo/tomoyo_path_chmod.md) - *Not Verified*
20. [tomoyo_path_chown](Tomoyo/tomoyo_path_chown.md) - *Not Verified*
21. [tomoyo_path_chroot](Tomoyo/tomoyo_path_chroot.md) - *Not Verified*
    
#### Mounting
22. [tomoyo_sb_mount](Tomoyo/tomoyo_sb_mount.md)  - *Not Verified*
23. [tomoyo_sb_umount](Tomoyo/tomoyo_sb_umount.md)  - *Not Verified*
24. [tomoyo_sb_pivotroot](Tomoyo/tomoyo_sb_pivotroot.md)  - *Not Verified*
    
#### Network
25. [tomoyo_socket_bind](Tomoyo/tomoyo_socket_bind.md)  - *Not Verified*
26. [tomoyo_socket_connect](Tomoyo/tomoyo_socket_connect.md)  - *Not Verified*
27. [tomoyo_socket_listen](Tomoyo/tomoyo_socket_listen.md)  - *Not Verified*
28. [tomoyo_socket_sendmsg](Tomoyo/tomoyo_socket_sendmsg.md)  - *Not Verified*
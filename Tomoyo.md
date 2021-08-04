## **Tomoyo Hook Functions:**

#### Credentials
1. tomoyo_cred_alloc_blank
2. tomoyo_cred_prepare
3. tomoyo_cred_transfer
4. tomoyo_cred_free
   
#### Exec
5. tomoyo_bprm_set_creds
6. tomoyo_bprm_check_security
   
#### Paths & Files
7. tomoyo_file_fcntl
8. tomoyo_file_open
9. tomoyo_path_truncate 
10. tomoyo_path_unlink
11. tomoyo_path_mkdir
12. tomoyo_path_rmdir
13. tomoyo_path_symlin
14. tomoyo_path_mknod
15. tomoyo_path_link
16. tomoyo_path_renam
17. tomoyo_inode_getatt
18. tomoyo_file_ioct
19. tomoyo_path_chmo
20. tomoyo_path_chown
21. tomoyo_path_chroo
    
#### Mounting
22. tomoyo_sb_moun
23. tomoyo_sb_umount
24. tomoyo_sb_pivotroo
    
#### Network
25. tomoyo_socket_bind
26. tomoyo_socket_connect
27. tomoyo_socket_listen
28. tomoyo_socket_sendmsg
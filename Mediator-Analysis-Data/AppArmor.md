## **AppArmor Hook Functions:**

#### General
1. apparmor_ptrace_access_check
2. apparmor_ptrace_traceme
3. apparmor_capget
4. apparmor_capable
5. apparmor_task_setrlimit

#### Paths & Files
6. apparmor_path_link
7. apparmor_path_unlink
8. apparmor_path_symlink
9. apparmor_path_mkdir
10. apparmor_path_rmdir
11. apparmor_path_mknod
12. apparmor_path_rename
13. apparmor_path_chmod
14. apparmor_path_chown
15. apparmor_path_truncate
16. apparmor_inode_getatt
17. apparmor_file_open
18. apparmor_file_permission
19. apparmor_file_alloc_security
20. apparmor_file_free_security
21. apparmor_mmap_file
22. cap_mmap_addr
23. apparmor_file_mprotect
24. apparmor_file_lock

#### Process
25. apparmor_getprocattr
26. apparmor_setprocattr

#### Credentials
27. apparmor_cred_alloc_blank
28. apparmor_cred_free
29. apparmor_cred_prepare
30.  apparmor_cred_transfer

#### Exec
31. apparmor_bprm_set_creds
32. apparmor_bprm_committing_creds
33. apparmor_bprm_committed_creds
34. apparmor_bprm_secureexec
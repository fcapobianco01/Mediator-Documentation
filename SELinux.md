
## **SELinux Hook Functions:**

#### General

1. [selinux_ptrace_access]()
2. selinux_capget
3. selinux_capset
4. selinux_capable
5. selinux_quotactl
6. selinux_quota_on
7. selinux_syslog
8. selinux_vm_enough_memory
9. selinux_netlink_send

#### BPRM
10. selinux_bprm_set_creds
11. selinux_bprm_committing_creds
12. selinux_bprm_committed_creds
13. selinux_bprm_secureexec

#### Mounting
14. selinux_sb_alloc_security
15. selinux_sb_free_security
16. selinux_sb_copy_data
17. selinux_sb_remount
18. selinux_sb_kern_mount
19. selinux_sb_show_options
20. selinux_sb_statfs
21. selinux_mount
22. selinux_umount
23. selinux_set_mnt_opts
24. selinux_sb_clone_mnt_opts
25. selinux_parse_opts_str

#### Inode & Dentry
26. selinux_dentry_init_security
27. selinux_inode_alloc_security
28. selinux_inode_free_security
29. selinux_inode_init_security
30. selinux_inode_create
31. selinux_inode_link
32. selinux_inode_unlink
33. selinux_inode_symlink
34. selinux_inode_mkdir
35. selinux_inode_rmdir
36. selinux_inode_mknod
37. selinux_inode_rename
38. selinux_inode_readlink
39. selinux_inode_follow_link
40. selinux_inode_permission
41. selinux_inode_setattr
42. selinux_inode_getattr
43. selinux_inode_setxattr
44. selinux_inode_post_setxattr
45. selinux_inode_getxattr
46. selinux_inode_listxattr
47. Selinux_inode_removexattr
48. Selinux_inode_getsecurity
49. Selinux_inode_setsecurity
50. Selinux_inode_listsecurity
51. selinux_inode_getsecid

#### Files
52. selinux_file_permission
53. selinux_file_alloc_security
54. selinux_file_free_security
55. selinux_file_ioctl
56. selinux_mmap_file
57. selinux_mmap_addr
58. selinux_file_mprotect
59. selinux_file_lock
60. selinux_file_fcntl
61. selinux_file_set_fowner
62. selinux_file_send_sigiotas
63. selinux_file_receive
64. selinux_file_open

#### Tasks & Creds
65. selinux_task_create
66. selinux_cred_alloc_blank
67. selinux_cred_free
68. selinux_cred_prepare
69. selinux_cred_transfer
70. selinux_kernel_act_as
71. selinux_kernel_create_files_as
72. selinux_kernel_module_request
73. selinux_task_setpgid
74. selinux_task_getpgid
75. selinux_task_getsid
76. selinux_task_getsecid
77. selinux_task_setnice
78. selinux_task_setioprio
79. selinux_task_getioprio
80. selinux_task_setrlimit
81. selinux_task_setscheduler
82. selinux_task_getscheduler
83. selinux_task_movememory
84. selinux_task_kill
85. selinux_task_wait
86. selinux_task_to_inode

#### IPC
87. selinux_ipc_permission
88. selinux_ipc_getsecid

#### MSG
89. selinux_msg_msg_alloc_security
90. selinux_msg_msg_free_security
91. selinux_msg_queue_alloc_security
92. selinux_msg_queue_free_security
93. selinux_msg_queue_associate
94. selinux_msg_queue_msgctl
95. selinux_msg_queue_msgsnd
96. selinux_msg_queue_msgrcv

#### Shared Memory
97. selinux_shm_alloc_security
98. selinux_shm_free_security
99. selinux_shm_associate
100. selinux_shm_shmctl
101. selinux_shm_shmat

#### Semaphores
102. selinux_sem_alloc_security
103. selinux_sem_free_security
104. selinux_sem_associate
105. selinux_sem_semctl
106. selinux_sem_semop
107. selinux_d_instantiate
108. selinux_getprocattr
109. selinux_setprocattr
110. selinux_ismaclabel
111. selinux_secid_to_secctx
112. selinux_secctx_to_secid
113. selinux_release_secctx
114. selinux_inode_notifysecctx
115. selinux_inode_setsecctx
116. selinux_inode_getsecctx
117. selinux_socket_unix_stream_connect
118. selinux_socket_unix_may_send

#### Network Hooks
119. selinux_socket_create
120. selinux_socket_post_create
121. selinux_socket_bind
122. selinux_socket_connect
123. selinux_socket_listen
124. selinux_socket_accept
125. selinux_socket_sendmsg
126. selinux_socket_recvmsg
127. selinux_socket_getsockname
128. selinux_socket_getpeername
129. selinux_socket_getsockopt
130. selinux_socket_setsockopt
131. selinux_socket_shutdown
132. selinux_socket_sock_rcv_skb
133. selinux_socket_getpeersec_stream
134. selinux_socket_getpeersec_dgram
135. selinux_sk_alloc_security
136. selinux_sk_free_security
137. selinux_sk_clone_security
138. selinux_sk_getsecid
139. selinux_sock_graft
140. selinux_inet_conn_request
141. selinux_inet_csk_clone
142. selinux_inet_conn_established
143. selinux_secmark_relabel_packet
144. selinux_secmark_refcount_inc
145. selinux_secmark_refcount_dec
146. selinux_req_classify_flow
147. selinux_tun_dev_alloc_security
148. selinux_tun_dev_free_security
149. selinux_tun_dev_create
150. selinux_tun_dev_attach_queue
151. selinux_tun_dev_attach
152. selinux_tun_dev_open
153. selinux_skb_owned_by

#### Network XFRM
176. selinux_xfrm_policy_alloc
177. selinux_xfrm_policy_clone
178. selinux_xfrm_policy_free
179. selinux_xfrm_policy_delete
180. selinux_xfrm_state_alloc
181. selinux_xfrm_state_alloc_acquire
182. selinux_xfrm_state_free
183. selinux_xfrm_state_delete
184. selinux_xfrm_policy_lookup
185. selinux_xfrm_state_pol_flow_match
186. selinux_xfrm_decode_session

#### Keys
190. selinux_key_alloc
191. selinux_key_free
192. selinux_key_permission
193. selinux_key_getsecurity

#### Audit
196. selinux_audit_rule_init
197. selinux_audit_rule_known
198. selinux_audit_rule_match
199. selinux_audit_rule_free

# Relaxed Noninterference Cases

- [Relaxed Noninterference Cases](#relaxed-noninterference-cases)
  - [General Approach](#general-approach)
    - [Return 0](#return-0)
    - [Safe Relaxed Noninterference Case IIs](#safe-relaxed-noninterference-case-iis)
  - [Common set of annotations for relaxed noninterference](#common-set-of-annotations-for-relaxed-noninterference)
  - [Categorization of branches which create information flow gaps](#categorization-of-branches-which-create-information-flow-gaps)
    - [AppArmor](#apparmor)
      - [Return 0](#return-0-1)
      - [Relaxed NI - Safe Case II](#relaxed-ni---safe-case-ii)
      - [True gaps](#true-gaps)
      - [Non-branching related](#non-branching-related)
    - [Tomoyo](#tomoyo)
      - [Return 0](#return-0-2)
      - [Relaxed NI - Safe Case II](#relaxed-ni---safe-case-ii-1)
      - [True gaps](#true-gaps-1)
      - [Non-branching related](#non-branching-related-1)
    - [SELinux](#selinux)
      - [Return 0](#return-0-3)
      - [Relaxed NI - Safe Case II](#relaxed-ni---safe-case-ii-2)
      - [True gaps](#true-gaps-2)
      - [Non-branching related](#non-branching-related-2)
      - [False positives](#false-positives)
      - [Valid flows](#valid-flows)
      - [Non-implicit related](#non-implicit-related)
  - [*Case-by-case notes*](#case-by-case-notes)
    - [`selinux_sem_semctl`, `selinux_shm_shmctl`, `selinux_msg_queue_msgctl`](#selinux_sem_semctl-selinux_shm_shmctl-selinux_msg_queue_msgctl)
    - [Lines removed with relaxed noninterference update](#lines-removed-with-relaxed-noninterference-update)
    - [old relaxed - new relaxed](#old-relaxed---new-relaxed)
    - [SELinux](#selinux-1)
    - [Tomoyo](#tomoyo-1)
    - [AppArmor](#apparmor-1)

## General Approach

There are two categories of source code lines which we need to annotate with relaxed noninterference, [return 0 cases](#return-0) and [safe case IIs](#safe-relaxed-noninterference-case-iis).

### Return 0

In a CFG, a return 0 statement is a return statement that 1) returns a zero, and 2) there is no sink call before it. Among all return 0 statements, some of them are conditionals, and we choose to annotate those conditional branches. We choose to annotate these scenarios because they are already reported as a relaxed NI case I violation. They wouldn't affect the subsequent analysis on case II violations.

### Safe Relaxed Noninterference Case IIs

In a CFG, we annotate a branch if there are no two paths after it that calls the same sink function or its wrapper, given they are safe based on relaxed NI case II.

## Common set of annotations for relaxed noninterference

This is the version where the return 0 cases are annotated to avoid affecting safe relaxed NI case 2's. The JSON object should be put into the config files in their corresponding LSMs.

```json
AppArmor
  "implicit_whitelist": [
    { "file": "security/apparmor/lsm.c", "line": 100 },
    { "file": "security/apparmor/lsm.c", "line": 109 },
    { "file": "security/apparmor/lsm.c", "line": 145 },
    { "file": "security/apparmor/lsm.c", "line": 229 },
    { "file": "security/apparmor/lsm.c", "line": 253 },
    { "file": "security/apparmor/lsm.c", "line": 288 },
    { "file": "security/apparmor/lsm.c", "line": 327 },
    { "file": "security/apparmor/lsm.c", "line": 396 },
    { "file": "security/apparmor/lsm.c", "line": 434 },
    { "file": "security/apparmor/lsm.c", "line": 435 },
    { "file": "security/apparmor/lsm.c", "line": 447 },
    { "file": "security/apparmor/lsm.c", "line": 448 },
    { "file": "security/apparmor/lsm.c", "line": 474 },
    { "file": "security/apparmor/lsm.c", "line": 308 },
    { "file": "security/apparmor/lsm.c", "line": 323 },
    { "file": "security/apparmor/lsm.c", "line": 349 },
    { "file": "security/apparmor/lsm.c", "line": 361 },
    { "file": "security/apparmor/lsm.c", "line": 369 },
    { "file": "security/apparmor/lsm.c", "line": 382 },
    { "file": "security/apparmor/lsm.c", "line": 435 }
  ],

Tomoyo
  "implicit_whitelist": [
    { "file": "security/tomoyo/file.c", "line": 565 },
    { "file": "security/tomoyo/file.c", "line": 701 },
    { "file": "security/tomoyo/file.c", "line": 702 },
    { "file": "security/tomoyo/file.c", "line": 750 },
    { "file": "security/tomoyo/file.c", "line": 758 },
    { "file": "security/tomoyo/file.c", "line": 761 },
    { "file": "security/tomoyo/file.c", "line": 797 },
    { "file": "security/tomoyo/file.c", "line": 798 },
    { "file": "security/tomoyo/file.c", "line": 814 },
    { "file": "security/tomoyo/file.c", "line": 852 },
    { "file": "security/tomoyo/file.c", "line": 853 },
    { "file": "security/tomoyo/file.c", "line": 898 },
    { "file": "security/tomoyo/file.c", "line": 899 },
    { "file": "security/tomoyo/mount.c", "line": 94 },
    { "file": "security/tomoyo/mount.c", "line": 102 },
    { "file": "security/tomoyo/mount.c", "line": 122 },
    { "file": "security/tomoyo/mount.c", "line": 132 },
    { "file": "security/tomoyo/mount.c", "line": 138 },
    { "file": "security/tomoyo/mount.c", "line": 147 },
    { "file": "security/tomoyo/network.c", "line": 473 },
    { "file": "security/tomoyo/network.c", "line": 474 },
    { "file": "security/tomoyo/network.c", "line": 509 },
    { "file": "security/tomoyo/network.c", "line": 517 },
    { "file": "security/tomoyo/network.c", "line": 548 },
    { "file": "security/tomoyo/network.c", "line": 549 },
    { "file": "security/tomoyo/network.c", "line": 560 },
    { "file": "security/tomoyo/network.c", "line": 596 },
    { "file": "security/tomoyo/tomoyo.c", "line": 126 },
    { "file": "security/tomoyo/tomoyo.c", "line": 315 },
    { "file": "security/tomoyo/tomoyo.c", "line": 382 }
  ],

SELinux
  "implicit_whitelist": [
    { "file": "include/linux/slab.h", "line": 522 },
    { "file": "security/selinux/hooks.c", "line": 636 },
    { "file": "security/selinux/hooks.c", "line": 647 },
    { "file": "security/selinux/hooks.c", "line": 665 },
    { "file": "security/selinux/hooks.c", "line": 666 },
    { "file": "security/selinux/hooks.c", "line": 734 },
    { "file": "security/selinux/hooks.c", "line": 1060 },
    { "file": "security/selinux/hooks.c", "line": 1246 },
    { "file": "security/selinux/hooks.c", "line": 1370 },
    { "file": "security/selinux/hooks.c", "line": 1611 },
    { "file": "security/selinux/hooks.c", "line": 1683 },
    { "file": "security/selinux/hooks.c", "line": 1694 },
    { "file": "security/selinux/hooks.c", "line": 1731 },
    { "file": "security/selinux/hooks.c", "line": 1829 },
    { "file": "security/selinux/hooks.c", "line": 1843 },
    { "file": "security/selinux/hooks.c", "line": 1942 },
    { "file": "security/selinux/hooks.c", "line": 1959 },
    { "file": "security/selinux/hooks.c", "line": 2008 },
    { "file": "security/selinux/hooks.c", "line": 2019 },
    { "file": "security/selinux/hooks.c", "line": 2611 },
    { "file": "security/selinux/hooks.c", "line": 2615 },
    { "file": "security/selinux/hooks.c", "line": 2852 },
    { "file": "security/selinux/hooks.c", "line": 2857 },
    { "file": "security/selinux/hooks.c", "line": 2869 },
    { "file": "security/selinux/hooks.c", "line": 2888 },
    { "file": "security/selinux/hooks.c", "line": 2917 },
    { "file": "security/selinux/hooks.c", "line": 2919 },
    { "file": "security/selinux/hooks.c", "line": 2944 },
    { "file": "security/selinux/hooks.c", "line": 2948 },
    { "file": "security/selinux/hooks.c", "line": 2959 },
    { "file": "security/selinux/hooks.c", "line": 2990 },
    { "file": "security/selinux/hooks.c", "line": 2995 },
    { "file": "security/selinux/hooks.c", "line": 3000 },
    { "file": "security/selinux/hooks.c", "line": 3055 },
    { "file": "security/selinux/hooks.c", "line": 3165 },
    { "file": "security/selinux/hooks.c", "line": 3169 },
    { "file": "security/selinux/hooks.c", "line": 3170 },
    { "file": "security/selinux/hooks.c", "line": 3241 },
    { "file": "security/selinux/hooks.c", "line": 3242 },
    { "file": "security/selinux/hooks.c", "line": 3253 },
    { "file": "security/selinux/hooks.c", "line": 3277 },
    { "file": "security/selinux/hooks.c", "line": 3280 },
    { "file": "security/selinux/hooks.c", "line": 3308 },
    { "file": "security/selinux/hooks.c", "line": 3309 },
    { "file": "security/selinux/hooks.c", "line": 3318 },
    { "file": "security/selinux/hooks.c", "line": 3328 },
    { "file": "security/selinux/hooks.c", "line": 3597 },
    { "file": "security/selinux/hooks.c", "line": 3608 },
    { "file": "security/selinux/hooks.c", "line": 3628 },
    { "file": "security/selinux/hooks.c", "line": 3639 },
    { "file": "security/selinux/hooks.c", "line": 3992 },
    { "file": "security/selinux/hooks.c", "line": 4048 },
    { "file": "security/selinux/hooks.c", "line": 4076 },
    { "file": "security/selinux/hooks.c", "line": 4109 },
    { "file": "security/selinux/hooks.c", "line": 4144 },
    { "file": "security/selinux/hooks.c", "line": 4145 },
    { "file": "security/selinux/hooks.c", "line": 4155 },
    { "file": "security/selinux/hooks.c", "line": 4160 },
    { "file": "security/selinux/hooks.c", "line": 4166 },
    { "file": "security/selinux/hooks.c", "line": 4315 },
    { "file": "security/selinux/hooks.c", "line": 4323 },
    { "file": "security/selinux/hooks.c", "line": 4344 },
    { "file": "security/selinux/hooks.c", "line": 4347 },
    { "file": "security/selinux/hooks.c", "line": 4355 },
    { "file": "security/selinux/hooks.c", "line": 4374 },
    { "file": "security/selinux/hooks.c", "line": 4390 },
    { "file": "security/selinux/hooks.c", "line": 4398 },
    { "file": "security/selinux/hooks.c", "line": 4409 },
    { "file": "security/selinux/hooks.c", "line": 4421 },
    { "file": "security/selinux/hooks.c", "line": 4717 },
    { "file": "security/selinux/hooks.c", "line": 4724 },
    { "file": "security/selinux/hooks.c", "line": 5070 },
    { "file": "security/selinux/hooks.c", "line": 5237 },
    { "file": "security/selinux/hooks.c", "line": 5244 },
    { "file": "security/selinux/hooks.c", "line": 5493 },
    { "file": "security/selinux/hooks.c", "line": 5519 },
    { "file": "security/selinux/hooks.c", "line": 5656 },
    { "file": "security/selinux/hooks.c", "line": 5567 },
    { "file": "security/selinux/hooks.c", "line": 5636 },
    { "file": "security/selinux/hooks.c", "line": 5671 },
    { "file": "security/selinux/hooks.c", "line": 5675 },
    { "file": "security/selinux/hooks.c", "line": 5594 },
    { "file": "security/selinux/hooks.c", "line": 5783 },
    { "file": "security/selinux/xfrm.c", "line": 89 },
    { "file": "security/selinux/xfrm.c", "line": 90 },
    { "file": "security/selinux/xfrm.c", "line": 91 },
    { "file": "security/selinux/xfrm.c", "line": 95 },
    { "file": "security/selinux/xfrm.c", "line": 99 },
    { "file": "security/selinux/xfrm.c", "line": 108 },
    { "file": "security/selinux/xfrm.c", "line": 144 },
    { "file": "security/selinux/xfrm.c", "line": 184 },
    { "file": "security/selinux/xfrm.c", "line": 192 },
    { "file": "security/selinux/xfrm.c", "line": 196 },
    { "file": "security/selinux/xfrm.c", "line": 202 }
  ],
```

## Categorization of branches which create information flow gaps

### AppArmor

#### Return 0

```c
lsm.c,229
lsm.c,253
lsm.c,288
lsm.c,327
lsm.c,396
lsm.c,434
lsm.c,435
lsm.c,447
lsm.c,448
lsm.c,474
```

```c
lsm.c:229 
  [common_perm_rm]
    apparmor_path_unlink
    apparmor_path_rmdir

lsm.c:253 
  [common_perm_create]
    apparmor_path_mkdir    
    apparmor_path_mknod
    apparmor_path_symlink

lsm.c:288
  apparmor_path_truncate

lsm.c:327
  apparmor_path_rename

lsm.c:396
  apparmor_file_open

lsm.c:434, 435  - One branch, two conditions
lsm.c:447, 448  - Another branch in the same function
  [common_file_perm]
    apparmor_file_permission
    apparmor_file_lock
    [common_mmap]
      apparmor_mmap_file
      apparmor_file_mprotect

lsm.c:474       - See case above, already covered.
  [common_mmap]
```

#### Relaxed NI - Safe Case II

```c
lsm.c,100
lsm.c,109
lsm.c,145
```

#### True gaps

```c
file.h,200
file.h,202
file.h,205
file.h,208
file.h,210
lsm.c,463
lsm.c,477
lsm.c,483
lsm.c,485
lsm.c,501
```

#### Non-branching related

```c
apparmor.h,117
```

This happened to be a coincidence of capturing the `tobool` in the `mediated_filesystem` function calls scattered in the code. A failed check indicates a returning 0 scenario, but the branch is not at the location above. So it's not possible to annotate those branches from the source location above. Rather, we need to annotate the following source locations in a more aggressive way.

```c
lsm.c,308
lsm.c,323
lsm.c,349
lsm.c,361
lsm.c,369
lsm.c,382
lsm.c,435
```

### Tomoyo

#### Return 0

```c
file.c,565
file.c,701
file.c,702
file.c,750
file.c,758
file.c,761
file.c,797
file.c,798
file.c,852
file.c,853
file.c,898
file.c,899
tomoyo.c,315
tomoyo.c,382
network.c,473
network.c,474
network.c,509
network.c,517
network.c,548
network.c,549
network.c,596
```

```c
file.c:565
  [tomoyo_path_permission]
    [tomoyo_check_open_permission]
      tomoyo_bprm_check_security
      tomoyo_file_fcntl
      tomoyo_file_open
    [tomoyo_path_perm]
      tomoyo_inode_getattr
      tomoyo_path_truncate
      tomoyo_path_unlink
      tomoyo_path_rmdir
      tomoyo_path_symlink
      tomoyo_path_chroot
      tomoyo_sb_umount

file.c:701,702
  [tomoyo_path_number_perm]
    tomoyo_file_ioctl
    tomoyo_path_chmod
    tomoyo_path_chown
    tomoyo_path_mkdir
    tomoyo_path_mknod

file.c:750 - covered above
file.c:758
file.c:761
  [tomoyo_check_open_permission]

file.c:797,798 - covered above
  [tomoyo_path_perm]

file.c:852,853
  tomoyo_mkdev_perm

file.c:898,899
  [tomoyo_path2_perm]
    tomoyo_path_link
    tomoyo_path_rename
    tomoyo_sb_pivotroot

tomoyo.c:315
  tomoyo_file_fcntl

tomoyo.c:382
  tomoyo_path_chown

network.c:473,474
network.c:509
network.c:517
  [tomoyo_inet_entry]
    [tomoyo_check_inet_address]
      tomoyo_socket_bind_permission
      tomoyo_socket_connect_permission
      tomoyo_socket_listen_permission
      tomoyo_socket_sendmsg_permission

network.c:548,549
  [tomoyo_unix_entry]
    [tomoyo_check_unix_address]
      SAME FOUR HOOKS

network.c:596 - covered above
  [tomoyo_check_unix_address]
```

#### Relaxed NI - Safe Case II

```c
file.c,814
tomoyo.c,126
mount.c,94
mount.c,102
mount.c,122
mount.c,132
mount.c,138
mount.c,147
network.c,560
```

#### True gaps

```c
file.c,762
mount.c,112
mount.c,115
network.c,527
```

#### Non-branching related

```c
network.c,478
uidgid.h,50
```

### SELinux

#### Return 0

```c
hooks.c,1611
hooks.c,3253
hooks.c,3165
hooks.c,3169
hooks.c,3170
hooks.c,2852
hooks.c,2857
hooks.c,5783
hooks.c,2888
hooks.c,5493
hooks.c,3280
hooks.c,4724
hooks.c,2019
hooks.c,2615
hooks.c,4144
hooks.c,4145
hooks.c,4374
hooks.c,4355
hooks.c,3628
xfrm.c,144
xfrm.c,192
```

```c
hooks.c:1611
  [inode_has_perm]
    [dentry_has_perm]
      selinux_quota_on
      selinux_inode_readlink
      selinux_inode_follow_link
      selinux_inode_setattr
      selinux_inode_setotherxattr
      selinux_inode_getxattr
      selinux_inode_listxattr
    [path_has_perm]
      selinux_mount
      selinux_inode_getattr
    [file_path_has_perm]
      selinux_file_open
    [file_has_perm]
      [selinux_revalidate_file_permission]
        selinux_file_permission
      selinux_file_ioctl
      [file_map_prot_check]
        selinux_mmap_file
        selinux_file_mprotect
      selinux_file_mprotect
      selinux_file_lock
      selinux_file_fcntl
      selinux_file_receive

hooks.c:3253 - covered
  [file_map_prot_check]

hooks.c:3165
hooks.c:3169,3170
  selinux_file_permission
  
hooks.c:2852
hooks.c:2857
  selinux_inode_permission

hooks.c:2888
  selinux_inode_setattr
  
hooks.c:5783
  selinux_key_permission

hooks.c:5493
  selinux_ipc_permission

hooks.c:3280
  selinux_mmap_addr

hooks.c:4724
  [selinux_nlmsg_perm]
    selinux_netlink_send

hooks.c:2019
  selinux_quotactl

hooks.c:2615
  selinux_sb_kern_mount

hooks.c:4144,4145
  selinux_socket_connect

hooks.c:4374
  selinux_socket_sock_rcv_skb
  
hooks.c:3628
  selinux_task_setrlimit

xfrm.c:144
  [selinux_xfrm_delete]
    selinux_xfrm_policy_delete
    selinux_xfrm_state_delete

xfrm.c:192
  selinux_xfrm_state_pol_flow_match
```

#### Relaxed NI - Safe Case II

```c
include/linux/slab.h,522
hooks.c,2008
hooks.c,1683
hooks.c,1694
hooks.c,3309
hooks.c,3308
hooks.c,3241
hooks.c,3242
hooks.c,3318
hooks.c,3328
hooks.c,1731
hooks.c,2869
hooks.c,5519
hooks.c,2919
hooks.c,3055
hooks.c,1829
hooks.c,1843
hooks.c,3639
hooks.c,2944
hooks.c,2948
hooks.c,2917
hooks.c,2990
hooks.c,3000
hooks.c,5244
hooks.c,5237
hooks.c,4717
hooks.c,1942
hooks.c,1959
hooks.c,647
hooks.c,1370
hooks.c,1060
hooks.c,2611
hooks.c,1246
hooks.c,734
hooks.c,636
hooks.c,666
hooks.c,5567
hooks.c,5594
hooks.c,4048
hooks.c,4109
hooks.c,4160
hooks.c,4166
hooks.c,3992
hooks.c,4398
hooks.c,4323
hooks.c,4315
hooks.c,4344
hooks.c,4409
hooks.c,3608
hooks.c,3597
hooks.c,4347
hooks.c,5671
hooks.c,5636
xfrm.c,108
xfrm.c,89
xfrm.c,184

hooks.c,5640
```

#### True gaps

```c
hooks.c,159
hooks.c,144
hooks.c,3350
hooks.c,3258
hooks.c,3311
hooks.c,3312
hooks.c,3314
hooks.c,1904
hooks.c,1905
hooks.c,1886
hooks.c,1882
hooks.c,1890
hooks.c,1880
hooks.c,3151
hooks.c,3403
hooks.c,1874
hooks.c,1838
hooks.c,1848
hooks.c,1776
hooks.c,2896
hooks.c,2885
hooks.c,2963
hooks.c,5488
hooks.c,5490
hooks.c,2641
hooks.c,1945
hooks.c,5600
hooks.c,5580
hooks.c,4058
hooks.c,4068
hooks.c,4153
hooks.c,4169
hooks.c,3747
hooks.c,3661
hooks.c,3665
hooks.c,1888
hooks.c,1728
hooks.c,5578
hooks.c,4401
hooks.c,3790
hooks.c,3731
hooks.c,3261
hooks.c,3316
xfrm.c,411
xfrm.c,415
xfrm.h,35
```

#### Non-branching related

```c
hooks.c,1815
hooks.c,1845
hooks.c,3296
```

#### False positives

Just simple false positive from DSA messing up stuff.

```c
hooks.c,666       - Removed some FPs, rest are also false positives
hooks.c,443       - Latent false positives, lookup selinux_sb_kern_mount gaps
hooks.c,674       - Latent false positives, lookup selinux_sb_kern_mount gaps
hooks.c,770       - Latent false positives, lookup selinux_sb_kern_mount gaps
hooks.c,1346      - Latent false positives, lookup selinux_sb_kern_mount gaps
hooks.c,1388      - Latent false positives, lookup selinux_sb_kern_mount gaps
hooks.c,1454      - Latent false positives, lookup selinux_sb_kern_mount gaps
```

```c
include/linux/slab.h,522    - Subsequent code has no sink call, but is complicated
hooks.c,636
hooks.c,647                 - Removed some FPs, rest are also false positives
hooks.c,665
hooks.c,666                 - Removed some FPs, rest are also false positives
hooks.c,734                 - Early return but not zero
hooks.c,1060                - Early return but not zero
hooks.c,1246                - Subsequent code has no sink call, but is complicated
hooks.c,1611                - May not be end result return 0, as is a sink deep in call graph
hooks.c,1694                - Already have a potentially called sink before this branch
hooks.c,1731                - Already have a called sink before this branch
hooks.c,1843                - Already have a called sink before this branch
hooks.c,1942
hooks.c,1959
hooks.c,2008
hooks.c,2019
hooks.c,2611                - Early return but not zero
hooks.c,2615
hooks.c,2852
hooks.c,2857
hooks.c,2869                - Already have a called sink before this branch
hooks.c,2888
hooks.c,2948                - Already have a called sink before this branch
hooks.c,2959                - Already have a called sink before this branch
hooks.c,2990                - Already have a called sink before this branch
hooks.c,2995                - Already have a called sink before this branch
hooks.c,3000                - Already have a called sink before this branch
hooks.c,3055                - Early return but not zero
hooks.c,3165
hooks.c,3169
hooks.c,3170
hooks.c,3253                - Already have a potentially called sink before this branch, must be success
hooks.c,3277                - Early return but not zero
hooks.c,3280
hooks.c,3328                - Already have a called sink before this branch
hooks.c,3597                - Early return but not zero
hooks.c,3608
hooks.c,3628
hooks.c,3639                - Early return but not zero
hooks.c,4048                - Already have a called sink before this branch
hooks.c,4076                - Early return but not zero
hooks.c,4109                - Early return but not zero
hooks.c,4155                - Early return but not zero
hooks.c,4160                - Already have a called sink before this branch
hooks.c,4166                - Already have a called sink before this branch
hooks.c,4315                - Early return but not zero
hooks.c,4323                - Early return but not zero
hooks.c,4344                - Early return but not zero
hooks.c,4355                - Return non-zero, dead code return
hooks.c,4374
hooks.c,4390                - Already have a called sink before this branch
hooks.c,4398                - Early return but not zero
hooks.c,4409                - Early return but not zero
hooks.c,4421                - Already have a called sink before this branch
hooks.c,4717
hooks.c,4724
hooks.c,5070                - Early return but not zero
hooks.c,5244
hooks.c,5493
hooks.c,5519                - Subsequent code has no sink call, but is complicated
hooks.c,5656                - Already have a called sink before this branch
hooks.c,5567                - Early return but not zero
hooks.c,5675                - Already have a called sink before this branch
hooks.c,5783
xfrm.c,89                   - Early return but not zero
xfrm.c,90                   - Early return but not zero
xfrm.c,91                   - Early return but not zero
xfrm.c,95                   - Early return but not zero
xfrm.c,99                   - Early return but not zero
xfrm.c,108                  - Early return but not zero
xfrm.c,144
xfrm.c,184                  - Early return but not zero
xfrm.c,192
xfrm.c,196
xfrm.c,202
```

#### Valid flows

They are true positive flows which affects sink argument values.

```c
hooks.c,144
hooks.c,159
hooks.c,1683      - Failing branch check leads to another branch where only one path goes to another sink
hooks.c,1728      - Is bypass
hooks.c,1829      - Subsequent code contains sink calls
hooks.c,1838
hooks.c,1874
hooks.c,1880
hooks.c,1882
hooks.c,1886
hooks.c,1888
hooks.c,1890
hooks.c,1904
hooks.c,1905
hooks.c,1945
hooks.c,2641
hooks.c,2885      - Does not lead to a DIRECT early return (ref:2888)
hooks.c,2896
hooks.c,2917      - Does not lead to a DIRECT early return
hooks.c,2919      - Does not lead to a DIRECT early return
hooks.c,2944
hooks.c,2963
hooks.c,3151
hooks.c,3242
hooks.c,3296
hooks.c,3308
hooks.c,3309
hooks.c,3311
hooks.c,3312
hooks.c,3314
hooks.c,3318
hooks.c,3350      - The fallthrough
hooks.c,3403
hooks.c,3661
hooks.c,3665
hooks.c,3715
hooks.c,3731
hooks.c,3747
hooks.c,3790
hooks.c,4058
hooks.c,4068
hooks.c,4153
hooks.c,4169
hooks.c,4347
hooks.c,4401
hooks.c,5237
hooks.c,5488
hooks.c,5490
hooks.c,5578
hooks.c,5600
hooks.c,5636
hooks.c,5671
xfrm.c,411
xfrm.c,415
xfrm.h,35
```

#### Non-implicit related

`cmp` and `tobool` variables not related to implicit flows. Rarely exists, but do show up in some code patterns.

```c
hooks.c,1776
hooks.c,1815
hooks.c,1845
hooks.c,1848
```

## *Case-by-case notes*

### `selinux_sem_semctl`, `selinux_shm_shmctl`, `selinux_msg_queue_msgctl`

Returning 0 when `cmd` is not in the set of expected values.

### Lines removed with relaxed noninterference update

```json
1611
1683
1694
3350
```

189 total relaxed annotations for previous version.
117 for tomoyo, reduced to 31.

`selinux_syslog` Should this one be annotated? current are the same, but appear at different places.

`selinux_inode_link` This is a FP because of the implicit assignment in IR at 1797

`file_map_prot_check` Visit this function.

`selinux_file_mprotect` 3328 questionable.

`selinux_quotactl` 2036, explicitly states */\* let the kernel handle invalid cmds \*/*

`selinux_netlink_send` always return 0 on 5069

`selinux_sb_kern_mount` 2614, */\* Allow all mounts performed by the kernel \*/*

`selinux_task_setrlimit` return explicit 0 when the old_limit equals new_limit on their max value.

`apparmor_file_lock` lsm.c:463, in theory, this branch should not be relaxed, but...

`may_create`

questionable `selinux` lines/hooks: 1565, 5519, 1728, 1731, 2885, 4724, `selinux_inode_setxattr`, `selinux_socket_bind`(4068, 4073)

### old relaxed - new relaxed

### SELinux

confirmed - `selinux_secmark_enabled(), selinux_authorizable_xfrm(x), IS_PRIVATE(inode)`, family of `capable`

```json
1611
3253
3165
5519
2852
5783
```

questionable

```json
1683
1694
3169
4724
4374
4401
3628
```

should be removed without question

```json
1565
3350
1902
1904
1905
1945
1874
5488
5490
4058
4068
4073
4048
```

### Tomoyo

confirmed - `tomoyo_init_request_info`

```json
750
565
797
898
899

```

questionable

```json
315 - tomoyo.c
379 - tomoyo.c
382 - tomoyo.c
596 - network.c
509,517 - network.c
```

should be removed without question

```json
126
807
110-117 - mount.c
```

### AppArmor

confirmed - `mediated_filesystem`, `unconfined`, `cap_ptrace_access_check`, `cap_ptrace_traceme`

```json
434, 435
438
447
396
382
369
349
```

questionable

```json
448
```

should be removed without question

```json
463
477
483
485
```

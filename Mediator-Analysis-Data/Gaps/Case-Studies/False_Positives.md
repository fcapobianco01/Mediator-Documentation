### SELinux

#### `selinux_shm_shmctl`
Tainting constant `i32 1` as external operation results in creating a path to object sink because there is a call `avc_has_perm(sid, SECINITSID_KERNEL, SECCLASS_SYSTEM, perms, NULL);` in `task_has_system()` and `SECINITSID_KERNEL` is defined as 1 in a macro. 

---

#### `selinux_inode_permission`
GEP to get `sclass` has `i32 4` as the index from `isec`. 

---
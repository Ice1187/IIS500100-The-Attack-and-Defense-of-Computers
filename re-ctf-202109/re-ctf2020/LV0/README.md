## strace
Run `strace` with option `-s 40` to print all the flag.

```
$ strace -s 40 ./strace
execve("./strace", ["./strace"], 0x7fffb372fd20 /* 15 vars */) = 0
uname({sysname="Linux", nodename="5a51e81951bc", ...}) = 0
brk(NULL)                               = 0x1270000
brk(0x12711c0)                          = 0x12711c0
arch_prctl(ARCH_SET_FS, 0x1270880)      = 0
readlink("/proc/self/exe", "/home/ice1187/IIS500100-The-Attack-and-D"..., 4096) = 95
brk(0x12921c0)                          = 0x12921c0
brk(0x1293000)                          = 0x1293000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
close(2)                                = 0
close(0)                                = 0
write(2, "FLAG{____yaaaa_flag_in_the_stack___}", 36) = -1 EBADF (Bad file descriptor)
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0x3), ...}) = 0
write(1, "find the flag in system call!\n", 30find the flag in system call!
) = 30
exit_group(0)                           = ?
+++ exited with 0 +++
```

Flag: `FLAG{____yaaaa_flag_in_the_stack___}`

## hexable
```
$ strings hexable
Can you find the flag?
easyctf{abcdef__123456}
```

Flag: `easyctf{abcdef__123456}`

## hexedit
```
$ strings hexedit  | grep easyctf
easyctf{eb04fadf}
```

Flag: `easyctf{eb04fadf}`

## LcukyGuess & adder
See `../basic/README.md`.

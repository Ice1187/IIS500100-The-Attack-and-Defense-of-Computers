# Procdump
```
$ /opt/volatility_2.6_lin64_standalone/volatility_2.6_lin64_standalone -f ../Triage-Memory.mem --profile=Win7SP1x64 procdump -p 3496 -D dumps/
Volatility Foundation Volatility Framework 2.6
Process(V)         ImageBase          Name                 Result
------------------ ------------------ -------------------- ------
0xfffffa8005a1d9e0 0x0000000000400000 UWkpjFjDzM.exe       OK: executable.3496.exe
```

# Not This
```
Offset(P)            #Ptr   #Hnd Access Name
------------------ ------ ------ ------ ----
0x000000000708e340     32      0 R--r-d \Device\HarddiskVolume2>￿dows\System32\drivers\dumpfve.sys
0x000000000709ca60     16      0 R--rwd \Device\HarddiskVolume2Ƶ￿υ婢￿Data\VMware\VMware Tools\manifest.txt
0x000000000709db30     15      0 R--r-d \Device\HarddiskVolume2\Windows\System32\en-US\cmd.exe.mui
0x000000000709ee20     17      1 R--r-d \Device\HarddiskVolume2\Windows\System32\en-US\wsock32.dll.mui
0x00000000070d9900     16      0 R--r-- \Device\HarddiskVolume2䲠Å￿υ婢￿\Fonts\vgafix.fon
0x00000000070e05d0     17      1 R--r-d \Device\HarddiskVolume2\Windows\System32\en-US\win32k.sys.mui
0x00000000070ee2d0      8      0 R--r-d \Device\HarddiskVolume2\Windows\System32\drivers\monitor.sys
0x00000000070ee4a0     16      0 R--r-- \Device\HarddiskVolume2쾀Ą￿셐ć￿\System32\FNTCACHE.DAT
0x00000000070f32c0     32      0 R--r-d \Device\HarddiskVolume2쥰ѧ￿�>￿\System32\drivers\Diskdump.sys
0x000000000710add0      9      0 R--r-d \Device\HarddiskVolume2ႠѨ￿荰Ò￿\System32\tsddd.dll
0x0000000007118070      6      0 RW-rwd \Device\HarddiskVolume2\$Directory
0x0000000007135070     16      0 R--r-d \Device\HarddiskVolume2\Windows\Microsoft.NET\Framework64\v4.0.30319\en-US\WorkflowServiceHostPerformanceCounters.dll.mui
0x0000000007135290     14      0 R--r-d \Device\HarddiskVolume2\Windows\System32\drivers\pacer.sys
0x00000000071354e0     16      0 R--r-d \Device\HarddiskVolume2\Windows\System32\en-US\azroles.dll.mui
0x0000000007135e60     15      0 R--r-d \Device\HarddiskVolume2\Windows\System32\FWPUCLNT.DLL
0x0000000007136070     16      0 RW-rwd \Device\HarddiskVolume2\$Directory
0x0000000007136aa0     15      0 R--r-d \Device\HarddiskVolume2\Windows\System32\lsm.exe
0x0000000007136e20     16      0 R--r-d \Device\HarddiskVolume2\Windows\System32\drivers\en-US\pacer.sys.mui
```

```
$ grep -e UWkpjFjDzM.exe -e hfs.exe -e wscript.exe filescan.txt
0x000000013e246530      9      0 R--r-- \Device\HarddiskVolume2\Windows\SysWOW64\wscript.exe
0x000000013e24d910     16      0 R--r-d \Device\HarddiskVolume2\Windows\SysWOW64\en-US\wscript.exe.mui
0x000000013e252e60      4      0 R--r-d \Device\HarddiskVolume2\Windows\SysWOW64\wscript.exe
0x000000013e255f20     13      0 R--r-d \Device\HarddiskVolume2\Users\Bob\AppData\Local\Temp\rad93398.tmp\UWkpjFjDzM.exe
0x000000013e48e2b0      1      0 R--r-d \Device\HarddiskVolume2\Windows\SysWOW64\wscript.exe
0x000000013e508200      1      1 R--r-d \Device\HarddiskVolume2\Windows\SysWOW64\en-US\wscript.exe.mui
0x000000013e55cac0      1      1 R--r-d \Device\HarddiskVolume2\Windows\SysWOW64\wscript.exe
0x000000013e86a830      6      0 R--r-d \Device\HarddiskVolume2\Users\Bob\Desktop\hfs.exe
```

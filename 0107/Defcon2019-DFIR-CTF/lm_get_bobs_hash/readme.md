```
$ /opt/volatility_2.6_lin64_standalone/volatility_2.6_lin64_standalone -f ../Triage-Memory.mem --profile=Win7SP1x64 hivelist
Volatility Foundation Volatility Framework 2.6
Virtual            Physical           Name
------------------ ------------------ ----
0xfffff8a003ad2010 0x0000000125598010 \??\C:\System Volume Information\Syscache.hve
0xfffff8a00469c010 0x00000000a779d010 \SystemRoot\System32\Config\DEFAULT
0xfffff8a00000e010 0x00000000a9740010 [no name]
0xfffff8a000024010 0x00000000a97cb010 \REGISTRY\MACHINE\SYSTEM
0xfffff8a000053320 0x00000000a977a320 \REGISTRY\MACHINE\HARDWARE
0xfffff8a0000fe010 0x00000000a9625010 \SystemRoot\System32\Config\SECURITY
0xfffff8a0004db010 0x00000000a8599010 \Device\HarddiskVolume1\Boot\BCD
0xfffff8a00054b010 0x00000000a7fe3010 \SystemRoot\System32\Config\SOFTWARE
0xfffff8a000e66010 0x000000009ce84010 \SystemRoot\System32\Config\SAM
0xfffff8a000efe410 0x000000009be5c410 \??\C:\Windows\ServiceProfiles\NetworkService\NTUSER.DAT
0xfffff8a000f43010 0x000000009ba60010 \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT
0xfffff8a00125d010 0x000000009635a010 \??\C:\Users\Bob\AppData\Local\Microsoft\Windows\UsrClass.dat
0xfffff8a0012ea010 0x0000000096937010 \??\C:\Users\Bob\ntuser.dat
```

```
/opt/volatility_2.6_lin64_standalone/volatility_2.6_lin64_standalone -f ../Triage-Memory.mem --profile=Win7SP1x64 hashdump -y 0xfffff8a000024010 -s 0xfffff8a000e66010
Volatility Foundation Volatility Framework 2.6
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Bob:1000:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

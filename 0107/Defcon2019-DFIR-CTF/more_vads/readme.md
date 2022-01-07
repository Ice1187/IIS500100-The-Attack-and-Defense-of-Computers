```
$ /opt/volatility_2.6_lin64_standalone/volatility_2.6_lin64_standalone -f ../Triage-Memory.mem --profile=Win7SP1x64 vadinfo | grep 'Start 0x00000000033c0000 End 0x00000000033dffff'  -A 5
Volatility Foundation Volatility Framework 2.6
VAD node @ 0xfffffa80052652b0 Start 0x00000000033c0000 End 0x00000000033dffff Tag VadS
Flags: CommitCharge: 32, PrivateMemory: 1, Protection: 24
Protection: PAGE_NOACCESS
Vad Type: VadNone
```

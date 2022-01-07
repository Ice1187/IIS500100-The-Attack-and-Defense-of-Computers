```
$ /opt/volatility_2.6_lin64_standalone/volatility_2.6_lin64_standalone -f ../Triage-Memory.mem --profile=Win7SP1x64 vadinfo | grep 0xfffffa800577ba10  -A 5
Volatility Foundation Volatility Framework 2.6
VAD node @ 0xfffffa800577ba10 Start 0x0000000000030000 End 0x0000000000033fff Tag Vad
Flags: NoChange: 1, Protection: 1
Protection: PAGE_READONLY
Vad Type: VadNone
ControlArea @fffffa8005687a50 Segment fffff8a000c4f870
NumberOfSectionReferences:          1 NumberOfPfnReferences:           0
```

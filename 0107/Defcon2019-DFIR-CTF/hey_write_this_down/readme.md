```
$ /opt/volatility_2.6_lin64_standalone/volatility_2.6_lin64_standalone -f ../Triage-Memory.mem --profile=Win7SP1x64 pslist
Volatility Foundation Volatility Framework 2.6
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xfffffa8003c72b30 System                    4      0     87      547 ------      0 2019-03-22 05:31:55 UTC+0000
0xfffffa8004616040 smss.exe                252      4      2       30 ------      0 2019-03-22 05:31:55 UTC+0000
0xfffffa80050546b0 csrss.exe               332    324     10      516      0      0 2019-03-22 05:31:58 UTC+0000
0xfffffa800525a9e0 csrss.exe               372    364     11      557      1      0 2019-03-22 05:31:58 UTC+0000
0xfffffa8005259060 wininit.exe             380    324      3       78      0      0 2019-03-22 05:31:58 UTC+0000
0xfffffa8005268b30 winlogon.exe            416    364      3      110      1      0 2019-03-22 05:31:58 UTC+0000
0xfffffa8005680910 services.exe            476    380     12      224      0      0 2019-03-22 05:31:59 UTC+0000
0xfffffa80056885e0 lsass.exe               484    380      7      650      0      0 2019-03-22 05:32:00 UTC+0000
0xfffffa8005696b30 lsm.exe                 492    380     10      155      0      0 2019-03-22 05:32:00 UTC+0000
0xfffffa80056e1060 svchost.exe             592    476      9      375      0      0 2019-03-22 05:32:01 UTC+0000
0xfffffa800570d060 svchost.exe             672    476      7      341      0      0 2019-03-22 05:32:02 UTC+0000
0xfffffa800575e5b0 svchost.exe             764    476     20      447      0      0 2019-03-22 05:32:02 UTC+0000
0xfffffa8005775b30 svchost.exe             796    476     15      368      0      0 2019-03-22 05:32:03 UTC+0000
0xfffffa800577db30 svchost.exe             820    476     33     1073      0      0 2019-03-22 05:32:03 UTC+0000
0xfffffa80057beb30 svchost.exe             932    476     10      568      0      0 2019-03-22 05:32:03 UTC+0000
0xfffffa80057e4560 svchost.exe             232    476     15      410      0      0 2019-03-22 05:32:03 UTC+0000
0xfffffa8005850a30 spoolsv.exe             864    476     12      279      0      0 2019-03-22 05:32:04 UTC+0000
0xfffffa800583db30 svchost.exe            1028    476     19      307      0      0 2019-03-22 05:32:05 UTC+0000
0xfffffa80058ed390 OfficeClickToR         1136    476     23      631      0      0 2019-03-22 05:32:05 UTC+0000
0xfffffa80059cb7c0 taskhost.exe           1276    476      8      183      1      0 2019-03-22 05:32:07 UTC+0000
0xfffffa80059cc620 taskeng.exe            1292    820      4       83      0      0 2019-03-22 05:32:07 UTC+0000
0xfffffa80059e6890 dwm.exe                1344    796      3       88      1      0 2019-03-22 05:32:07 UTC+0000
0xfffffa8003de39c0 explorer.exe           1432   1308     28      976      1      0 2019-03-22 05:32:07 UTC+0000
0xfffffa8005a324e0 FileZilla Serv         1476    476      9       81      0      1 2019-03-22 05:32:07 UTC+0000
0xfffffa8005af24e0 VGAuthService.         1768    476      3       89      0      0 2019-03-22 05:32:09 UTC+0000
0xfffffa8005b49890 vmtoolsd.exe           1828   1432      6      144      1      0 2019-03-22 05:32:10 UTC+0000
0xfffffa8005b4eb30 vmtoolsd.exe           1852    476     10      314      0      0 2019-03-22 05:32:11 UTC+0000
0xfffffa8005ba0620 ManagementAgen         1932    476     10      102      0      0 2019-03-22 05:32:11 UTC+0000
0xfffffa8005be12c0 FileZilla Serv         1996   1860      3       99      1      1 2019-03-22 05:32:12 UTC+0000
0xfffffa8005409060 dllhost.exe            2072    476     13      194      0      0 2019-03-22 05:32:14 UTC+0000
0xfffffa8005478060 msdtc.exe              2188    476     12      146      0      0 2019-03-22 05:32:15 UTC+0000
0xfffffa80054d2380 WmiPrvSE.exe           2196    592     11      222      0      0 2019-03-22 05:32:15 UTC+0000
0xfffffa8005508650 SearchIndexer.         2456    476     13      766      0      0 2019-03-22 05:32:17 UTC+0000
0xfffffa80055b0060 wmpnetwk.exe           2628    476      9      210      0      0 2019-03-22 05:32:18 UTC+0000
0xfffffa8005c4ab30 svchost.exe            2888    476     11      152      0      0 2019-03-22 05:32:20 UTC+0000
0xfffffa80054f9060 notepad.exe            3032   1432      1       60      1      0 2019-03-22 05:32:22 UTC+0000
0xfffffa8005c8e440 WmiPrvSE.exe           2436    592      9      245      0      0 2019-03-22 05:32:33 UTC+0000
0xfffffa80053f83e0 EXCEL.EXE              1272   1432     21      789      1      1 2019-03-22 05:33:49 UTC+0000
0xfffffa80042aa430 cmd.exe                1408   1432      1       23      1      0 2019-03-22 05:34:12 UTC+0000
0xfffffa80042ab620 conhost.exe            1008    372      2       55      1      0 2019-03-22 05:34:12 UTC+0000
0xfffffa8004300620 taskeng.exe            1156    820      4       93      1      0 2019-03-22 05:34:14 UTC+0000
0xfffffa8004330b30 sppsvc.exe             3260    476      4      149      0      0 2019-03-22 05:34:15 UTC+0000
0xfffffa800432f060 svchost.exe            3300    476     13      346      0      0 2019-03-22 05:34:15 UTC+0000
0xfffffa800474c060 OUTLOOK.EXE            3688   1432     30     2023      1      1 2019-03-22 05:34:37 UTC+0000
0xfffffa800474fb30 taskmgr.exe            3792   1432      6      134      1      0 2019-03-22 05:34:38 UTC+0000
0xfffffa8005d067d0 StikyNot.exe           1628   1432      8      183      1      0 2019-03-22 05:34:42 UTC+0000
0xfffffa8004798320 calc.exe               3548   1432      3       77      1      0 2019-03-22 05:34:43 UTC+0000
0xfffffa80047cb060 iexplore.exe           3576    592     12      403      1      1 2019-03-22 05:34:48 UTC+0000
0xfffffa80047e9540 iexplore.exe           2780   3576      6      233      1      1 2019-03-22 05:34:48 UTC+0000
0xfffffa8004905620 hfs.exe                3952   1432      6      214      1      1 2019-03-22 05:34:51 UTC+0000
0xfffffa80053d3060 POWERPNT.EXE           4048   1432     23      765      1      1 2019-03-22 05:35:09 UTC+0000
0xfffffa8004083880 FTK Imager.exe         3192   1432      6      353      1      0 2019-03-22 05:35:12 UTC+0000
0xfffffa80042dbb30 chrome.exe             3248   1432     32      841      1      0 2019-03-22 05:35:14 UTC+0000
0xfffffa80047beb30 chrome.exe             3244   3248      7       91      1      0 2019-03-22 05:35:15 UTC+0000
0xfffffa80052f0060 chrome.exe             2100   3248      2       59      1      0 2019-03-22 05:35:15 UTC+0000
0xfffffa80053306f0 chrome.exe             1816   3248     14      328      1      0 2019-03-22 05:35:16 UTC+0000
0xfffffa8005300b30 chrome.exe             4156   3248     14      216      1      0 2019-03-22 05:35:17 UTC+0000
0xfffffa8005442b30 chrome.exe             4232   3248     14      233      1      0 2019-03-22 05:35:17 UTC+0000
0xfffffa8005419b30 chrome.exe             4240   3248     14      215      1      0 2019-03-22 05:35:17 UTC+0000
0xfffffa800540db30 chrome.exe             4520   3248     10      234      1      0 2019-03-22 05:35:18 UTC+0000
0xfffffa80053cbb30 chrome.exe             4688   3248     13      168      1      0 2019-03-22 05:35:19 UTC+0000
0xfffffa8005a80060 wscript.exe            5116   3952      8      312      1      1 2019-03-22 05:35:32 UTC+0000
0xfffffa8005a1d9e0 UWkpjFjDzM.exe         3496   5116      5      109      1      1 2019-03-22 05:35:33 UTC+0000
0xfffffa8005bb0060 cmd.exe                4660   3496      1       33      1      1 2019-03-22 05:35:36 UTC+0000
0xfffffa8005c1ab30 conhost.exe            4656    372      2       49      1      0 2019-03-22 05:35:36 UTC+0000
```

```
$ /opt/volatility_2.6_lin64_standalone/volatility_2.6_lin64_standalone -f ../Triage-Memory.mem --profile=Win7SP1x64 netscan
Volatility Foundation Volatility Framework 2.6
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0x13e057300        UDPv4    10.0.0.101:55736               *:*                                   2888     svchost.exe    2019-03-22 05:32:20 UTC+0000
0x13e05b4f0        UDPv6    ::1:55735                      *:*                                   2888     svchost.exe    2019-03-22 05:32:20 UTC+0000
0x13e05b790        UDPv6    fe80::7475:ef30:be18:7807:55734 *:*                                   2888     svchost.exe    2019-03-22 05:32:20 UTC+0000
0x13e05d4b0        UDPv6    fe80::7475:ef30:be18:7807:1900 *:*                                   2888     svchost.exe    2019-03-22 05:32:20 UTC+0000
0x13e05dec0        UDPv4    127.0.0.1:55737                *:*                                   2888     svchost.exe    2019-03-22 05:32:20 UTC+0000
0x13e05e3f0        UDPv4    10.0.0.101:1900                *:*                                   2888     svchost.exe    2019-03-22 05:32:20 UTC+0000
0x13e05eab0        UDPv6    ::1:1900                       *:*                                   2888     svchost.exe    2019-03-22 05:32:20 UTC+0000
0x13e064d70        UDPv4    127.0.0.1:1900                 *:*                                   2888     svchost.exe    2019-03-22 05:32:20 UTC+0000
0x13e02bcf0        TCPv4    -:49220                        72.51.60.132:443     CLOSED           4048     POWERPNT.EXE
0x13e035790        TCPv4    -:49223                        72.51.60.132:443     CLOSED           4048     POWERPNT.EXE
0x13e036470        TCPv4    -:49224                        72.51.60.132:443     CLOSED           4048     POWERPNT.EXE
0x13e258010        UDPv4    127.0.0.1:55560                *:*                                   5116     wscript.exe    2019-03-22 05:35:32 UTC+0000
0x13e305a50        UDPv4    0.0.0.0:5355                   *:*                                   232      svchost.exe    2019-03-22 05:32:09 UTC+0000
0x13e360be0        UDPv4    0.0.0.0:63790                  *:*                                   504                     2019-03-22 05:45:47 UTC+0000
0x13e490ec0        UDPv4    0.0.0.0:5355                   *:*                                   232      svchost.exe    2019-03-22 05:32:09 UTC+0000
0x13e490ec0        UDPv6    :::5355                        *:*                                   232      svchost.exe    2019-03-22 05:32:09 UTC+0000
0x13e5683e0        UDPv4    10.0.0.101:137                 *:*                                   4        System         2019-03-22 05:32:06 UTC+0000
0x13e594250        UDPv4    10.0.0.101:138                 *:*                                   4        System         2019-03-22 05:32:06 UTC+0000
0x13e597ec0        UDPv4    0.0.0.0:0                      *:*                                   232      svchost.exe    2019-03-22 05:32:06 UTC+0000
0x13e597ec0        UDPv6    :::0                           *:*                                   232      svchost.exe    2019-03-22 05:32:06 UTC+0000
0x13e61fb30        UDPv6    fe80::7475:ef30:be18:7807:546  *:*                                   764      svchost.exe    2019-03-22 05:46:23 UTC+0000
0x13e918010        UDPv4    0.0.0.0:56372                  *:*                                   1816     chrome.exe     2019-03-22 05:45:51 UTC+0000
0x13e9cd730        UDPv4    127.0.0.1:57374                *:*                                   1136     OfficeClickToR 2019-03-22 05:32:18 UTC+0000
0x13ea8e6a0        UDPv4    127.0.0.1:61704                *:*                                   3688     OUTLOOK.EXE    2019-03-22 05:34:44 UTC+0000
0x13ead0bf0        UDPv4    127.0.0.1:55614                *:*                                   4048     POWERPNT.EXE   2019-03-22 05:35:15 UTC+0000
0x13ebc6c20        UDPv4    0.0.0.0:5353                   *:*                                   3248     chrome.exe     2019-03-22 05:35:17 UTC+0000
0x13ebea890        UDPv4    0.0.0.0:5353                   *:*                                   3248     chrome.exe     2019-03-22 05:35:17 UTC+0000
0x13ebea890        UDPv6    :::5353                        *:*                                   3248     chrome.exe     2019-03-22 05:35:17 UTC+0000
0x13e2c6b10        TCPv4    0.0.0.0:21                     0.0.0.0:0            LISTENING        1476     FileZilla Serv
0x13e2c6b10        TCPv6    :::21                          :::0                 LISTENING        1476     FileZilla Serv
0x13e2c7850        TCPv6    ::1:14147                      :::0                 LISTENING        1476     FileZilla Serv
0x13e2c96b0        TCPv4    127.0.0.1:14147                0.0.0.0:0            LISTENING        1476     FileZilla Serv
0x13e2c9be0        TCPv4    0.0.0.0:21                     0.0.0.0:0            LISTENING        1476     FileZilla Serv
0x13e3a1150        TCPv4    0.0.0.0:49155                  0.0.0.0:0            LISTENING        484      lsass.exe
0x13e3a1150        TCPv6    :::49155                       :::0                 LISTENING        484      lsass.exe
0x13e3b2010        TCPv4    0.0.0.0:49155                  0.0.0.0:0            LISTENING        484      lsass.exe
0x13e430580        TCPv4    0.0.0.0:49154                  0.0.0.0:0            LISTENING        820      svchost.exe
0x13e430580        TCPv6    :::49154                       :::0                 LISTENING        820      svchost.exe
0x13e431820        TCPv4    0.0.0.0:49154                  0.0.0.0:0            LISTENING        820      svchost.exe
0x13e57e010        TCPv4    10.0.0.101:139                 0.0.0.0:0            LISTENING        4        System
0x13e71cef0        TCPv4    0.0.0.0:135                    0.0.0.0:0            LISTENING        672      svchost.exe
0x13e720660        TCPv4    0.0.0.0:135                    0.0.0.0:0            LISTENING        672      svchost.exe
0x13e720660        TCPv6    :::135                         :::0                 LISTENING        672      svchost.exe
0x13e72f010        TCPv4    0.0.0.0:49152                  0.0.0.0:0            LISTENING        380      wininit.exe
0x13e72f6e0        TCPv4    0.0.0.0:49152                  0.0.0.0:0            LISTENING        380      wininit.exe
0x13e72f6e0        TCPv6    :::49152                       :::0                 LISTENING        380      wininit.exe
0x13e770240        TCPv4    0.0.0.0:49153                  0.0.0.0:0            LISTENING        764      svchost.exe
0x13e772980        TCPv4    0.0.0.0:49153                  0.0.0.0:0            LISTENING        764      svchost.exe
0x13e772980        TCPv6    :::49153                       :::0                 LISTENING        764      svchost.exe
0x13ebb3010        TCPv4    0.0.0.0:49156                  0.0.0.0:0            LISTENING        476      services.exe
0x13ebb3010        TCPv6    :::49156                       :::0                 LISTENING        476      services.exe
0x13ebcdef0        TCPv4    0.0.0.0:80                     0.0.0.0:0            LISTENING        3952     hfs.exe
0x13e2348a0        TCPv4    -:49366                        192.168.206.181:389  CLOSED           504
0x13e397190        TCPv4    10.0.0.101:49217               10.0.0.106:4444      ESTABLISHED      3496     UWkpjFjDzM.exe
0x13e3986d0        TCPv4    -:49378                        213.209.1.129:25     CLOSED           504
0x13e3abae0        TCPv4    -:49226                        72.51.60.132:443     CLOSED           4048     POWERPNT.EXE
0x13e3e7010        TCPv6    -:0                            38db:7705:80fa:ffff:38db:7705:80fa:ffff:0 CLOSED           1136     OfficeClickToR
0x13e441830        TCPv6    -:0                            382b:c703:80fa:ffff:382b:c703:80fa:ffff:0 CLOSED           1        ?RK????
0x13e4e4910        TCPv4    10.0.0.101:49208               52.109.12.6:443      CLOSED           504
0x13e55fae0        TCPv4    10.0.0.101:49209               52.96.44.162:443     CLOSED           504
0x13e71b540        TCPv4    -:0                            104.208.112.5:0      CLOSED           1        ?RK????
0x13e73b560        TCPv4    -:49266                        35.190.69.156:443    CLOSED           504
0x13e7c6010        TCPv4    10.0.0.101:49204               172.217.6.195:443    CLOSED           1816     chrome.exe
0x13ead7cf0        TCPv4    10.0.0.101:49202               172.217.10.68:443    CLOSED           1816     chrome.exe
0x13f5898a0        TCPv4    0.0.0.0:49156                  0.0.0.0:0            LISTENING        476      services.exe
0x13f5899c0        TCPv4    0.0.0.0:445                    0.0.0.0:0            LISTENING        4        System
0x13f5899c0        TCPv6    :::445                         :::0                 LISTENING        4        System
0x13f4facf0        TCPv4    10.0.0.101:49262               52.109.12.6:443      ESTABLISHED      3688     OUTLOOK.EXE
0x13f50a010        TCPv4    -:49265                        213.186.33.3:443     CLOSED           504
0x13f5289f0        TCPv4    -:49234                        72.51.60.133:80      CLOSED           3688     OUTLOOK.EXE
0x13f7b4ec0        UDPv4    0.0.0.0:55707                  *:*                                   232      svchost.exe    2019-03-22 05:45:44 UTC+0000
0x13f7e8670        UDPv4    127.0.0.1:59411                *:*                                   3576     iexplore.exe   2019-03-22 05:34:49 UTC+0000
0x13fc6f1b0        UDPv4    0.0.0.0:55102                  *:*                                   232      svchost.exe    2019-03-22 05:45:36 UTC+0000
0x13fc78dc0        UDPv4    127.0.0.1:53361                *:*                                   1272     EXCEL.EXE      2019-03-22 05:34:03 UTC+0000
0x13f7ae010        TCPv4    10.0.0.101:49263               52.96.44.162:443     ESTABLISHED      3688     OUTLOOK.EXE
0x13fa93cf0        TCPv4    -:49173                        72.51.60.132:443     CLOSED           1272     EXCEL.EXE
0x13fa95cf0        TCPv4    -:49170                        72.51.60.132:443     CLOSED           1272     EXCEL.EXE
0x13fa969f0        TCPv4    -:0                            56.219.119.5:0       CLOSED           1272     EXCEL.EXE
0x13fbd07e0        TCPv4    -:49372                        212.227.15.9:25      CLOSED           504
0x13fc857e0        TCPv4    -:49167                        72.51.60.132:443     CLOSED           1272     EXCEL.EXE
```

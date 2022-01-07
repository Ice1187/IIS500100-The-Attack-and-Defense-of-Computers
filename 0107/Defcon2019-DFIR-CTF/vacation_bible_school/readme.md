```
$ /opt/volatility_2.6_lin64_standalone/volatility_2.6_lin64_standalone -f ../Triage-Memory.mem --profile=Win7SP1x64 memdump -p 5116 -D dumps
Volatility Foundation Volatility Framework 2.6
************************************************************************
Writing wscript.exe [  5116] to 5116.dmp
```

```
$ strings dumps/5116.dmp | grep vbs
"C:\Windows\System32\wscript.exe" //B //NOLOGO %TEMP%\vhjReUDEuumrX.vbs
%TEMP%\vhjReUDEuumrX.vbs
%TEMP%\vhjReUDEuumrX.vbs
```

## find
```
$ strings find | grep -E 'MyFirstCTF{[^{}]*}
'
MyFirstCTF{Y0U_gOt_th3_flag_bY_sTr1ngS}
```

Flag: `MyFirstCTF{Y0U_gOt_th3_flag_bY_sTr1ngS}`

## run-asm.asm
See `run-asm.py`.

Flag: `MyFirstCTF{C0mpi1e_aSm_4nd_RuN!}`

## reverse
Overflow to flip the condition to get the flag.
```
 8048456:       8d 45 b4                lea    eax,[ebp-0x4c]
 8048459:       50                      push   eax
 804845a:       e8 a1 fe ff ff          call   8048300 <gets@plt>
 804845f:       83 c4 10                add    esp,0x10
 8048462:       8b 45 f4                mov    eax,DWORD PTR [ebp-0xc]
 8048465:       85 c0                   test   eax,eax
 8048467:       74 12                   je     804847b <main+0x40>
```

```
$ ./reverse
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
BreakALLCTF{4U49uY7OJCrJL0vtbXjd}
```




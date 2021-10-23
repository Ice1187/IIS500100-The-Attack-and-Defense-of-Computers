### LuckyGuess

Run `luckguess.py` multiple times, when the answer is close to 50000000, it can get the answer.

Flag: `easyctf{aaA_tOucH_0f_luccK_47ca4e}`

### adder

3 number is added, then compare to 0x539, so provide it `0 0 1337` and get the flag.

```
   0x0000000000400b91 <+115>:   mov    edx,DWORD PTR [rbp-0xc]
   0x0000000000400b94 <+118>:   mov    eax,DWORD PTR [rbp-0x10]
   0x0000000000400b97 <+121>:   add    edx,eax
   0x0000000000400b99 <+123>:   mov    eax,DWORD PTR [rbp-0x14]
   0x0000000000400b9c <+126>:   add    eax,edx
   0x0000000000400b9e <+128>:   cmp    eax,0x539
   0x0000000000400ba3 <+133>:   jne    0x400bcc <main+174>
```

Flag: `easyctf{y0u_added_thr33_nums!}`

### 


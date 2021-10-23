## base64
Find the secret string.

```
$ strings base64
...
cHVzaCAweDdkMjEyMTIxCnB1c2ggMHg0NzZlNjk1MgpwdXNoIDB4NzQ1MzVmNjMKcHVzaCAweDMxNDczNDZkCnB1c2ggMHg1ZjQ0NmU2YwpwdXNoIDB4NDY1ZjU1MzAKcHVzaCAweDU5N2I0NjU0CnB1c2ggMHg0Mzc0NzM3MgpwdXNoIDB4Njk0Njc5NGQK
```

Use the program to decode it.
```
$ ./base64
I can decode base64
cHVzaCAweDdkMjEyMTIxCnB1c2ggMHg0NzZlNjk1MgpwdXNoIDB4NzQ1MzVmNjMKcHVzaCAweDMxNDczNDZkCnB1c2ggMHg1ZjQ0NmU2YwpwdXNoIDB4NDY1ZjU1MzAKcHVzaCAweDU5N2I0NjU0CnB1c2ggMHg0Mzc0NzM3MgpwdXNoIDB4Njk0Njc5NGQK
The output is
push 0x7d212121
push 0x476e6952
push 0x74535f63
push 0x3147346d
push 0x5f446e6c
push 0x465f5530
push 0x597b4654
push 0x43747372
push 0x6946794d
```

Write the script `base64.py` to get the flag.
```
$ python3 base64.py
b'MyFirstCTF{Y0U_FlnD_m4G1c_StRinG!!!}'
```

Flag: `MyFirstCTF{Y0U_FlnD_m4G1c_StRinG!!!}`

## 

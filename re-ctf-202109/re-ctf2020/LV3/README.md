## bin2.txt
The content of `bin2.txt` looks like assembly.
See the script `bin2.py`.

```
$ python3 bin2.py
   0:   48 b8 b5 a3 b9 b1 c6    movabs rax, 0x414141c6b1b9a3b5
   7:   41 41 41
   a:   50                      push   rax
   b:   48 b8 bc a0 a9 93 aa    movabs rax, 0x93bea3aa93a9a0bc
  12:   a3 be 93
  15:   50                      push   rax
  16:   48 b8 a9 93 a5 bf 93    movabs rax, 0xa1a5bf93bfa593a9
  1d:   bf a5 a1
  20:   50                      push   rax
  21:   48 b8 bf a4 a9 a0 a0    movabs rax, 0xa8a3afa0a0a9a4bf
  28:   af a3 a8
  2b:   50                      push   rax
  2c:   48 b8 8d 85 9f ff b7    movabs rax, 0x93a7a3b7ff9f858d
  33:   a3 a7 93
  36:   50                      push   rax
  37:   48 89 e6                mov    rsi, rsp
  3a:   48 31 d2                xor    rdx, rdx
  3d:   80 34 16 cc             xor    BYTE PTR [rsi+rdx*1], 0xcc
  41:   fe c2                   inc    dl
  43:   80 fa 25                cmp    dl, 0x25
  46:   75 f5                   jne    0x3d
  48:   48 31 c0                xor    rax, rax
  4b:   48 ff c0                inc    rax
  4e:   48 89 c7                mov    rdi, rax
  51:   0f 05                   syscall
  53:   6a 3c                   push   0x3c
  55:   58                      pop    rax
  56:   48 31 ff                xor    rdi, rdi
  59:   0f 05                   syscall
hex flag: [4702111807592571829, 10646126522167566524, 11647926652560053161, 12151749324000830655, 10639652655349073293]
Flag: b'AIS3{ok_shellcode_is_simple_for_you}'
```


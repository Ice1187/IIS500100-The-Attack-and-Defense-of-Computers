hex_flag = [
  0x7d212121,
  0x476e6952,
  0x74535f63,
  0x3147346d,
  0x5f446e6c,
  0x465f5530,
  0x597b4654,
  0x43747372,
  0x6946794d]

flag = b''
for f in hex_flag[::-1]:
	flag += f.to_bytes(4, 'little')

print(flag)

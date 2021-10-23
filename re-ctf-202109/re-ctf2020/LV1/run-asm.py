
hex_flag = [
  0x7d214e75,
  0x525f646e,
  0x345f6d53,
  0x615f6531,
  0x69706d30,
  0x437b4654,
  0x43747372,
  0x6946794d]

flag = b''
for f in hex_flag[::-1]:
	flag += f.to_bytes(4, 'little')

print(flag)

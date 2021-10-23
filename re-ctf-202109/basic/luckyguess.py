import socket

host = '127.0.0.1'
port = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def recv(info=None):
  res = s.recv(4096).decode('ascii')
  print(f'[<] {info if info else ""}')
  print(res)
  return res

def send(data):
  print(f'[>] {data}')
  data = str(data).encode('ascii')
  data = data + b'\n' if data[-1] != b'\n' else data
  s.send(data)

lo = 0
hi = 100000000
guess = hi
res = 'hi'
while 'hi' in res or 'lo' in res:
  send(guess)
  res = recv()
  if 'hi' in res:
    hi = guess
  elif 'lo' in res:
    lo = guess
  else:
    print(res)
    break
  guess = int((hi + lo) // 2)


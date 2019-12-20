import socket

s = socket.socket()
s.connect(('220.243.129.168',8433))
s.send('已连接'.encode('utf8'))
print(s.recv(1024).decode(encoding='utf8'))

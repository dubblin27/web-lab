import socket, sys 
s = socket.socket()
host = socket.gethostname() 
ip = socket.gethostbyname(host)
ip = int(input()) 
port = (int(input))
name = int(input())
s.connect((ip,port))
s.send(name.encode)
sname = s.recv(1024)
sname = sname.decode()
while True :
    mess = mess.recv(1024)
    mess = mess.decode()
    print(sname ,":", mess )
    smsg = input()
    s.send(smsg.encode())
    


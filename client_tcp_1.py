import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 2222))

while True:
    message = input()
    if message == "-end":
        break
    s.send(str.encode(message))
    rsp = s.recv(1024)
    print(rsp)


s.close()
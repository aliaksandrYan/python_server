import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 2222))

s.listen(10)


def thread_func():
    while True:
        conn, addr = s.accept()
        while True:
            data = conn.recv(1024)
            if not data or str(data) == "close":
                break
            conn.send(data)

        conn.close()


list_thread = [threading.Thread(target=thread_func) for _ in range(10)]

for _ in list_thread:
    _.start()
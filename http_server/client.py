import socket

HOST = "127.0.0.1"  # localhost
PORT = 8080  # Same as in server.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(b"Hello World!")
    response = sock.recv(1024)
print(f"Received {repr(response)}")

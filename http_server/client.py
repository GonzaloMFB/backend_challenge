import socket

HOST = "127.0.0.1"  # localhost
PORT = 8080  # Same as in server.

sample_req = "GET /path HTTP/1.1\r\nHost: Test Server\r\n\r\n"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(sample_req, encoding="utf-8"))
    response = sock.recv(1024)
print(f"Received {repr(response)}")

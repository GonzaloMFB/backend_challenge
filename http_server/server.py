import socket
from utils import http_parser

# HTTP Request:
# Line 0: Request line (e.g. GET /path HTTP/1.1)
# Line 1: Headers
# Line 2: -BLANK LINE- (separates headers from body)
# Line 3: Body (for requests like post)
body = "Hello world, this is a http message."
length = len(bytes(body, encoding="utf-8"))
sample_response = f"HTTP/1.1 200 OK\r\nServer: Test Server\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: {length}\r\n\r\n{body}"
sample_response = bytes(sample_response, encoding="utf-8")

# Define and bind socket
HOST = "127.0.0.1"  # localhost
PORT = 8080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                stream = conn.recv(1024)
                if not stream:
                    break
                res = http_parser(stream)
                print(res)
                conn.sendall(sample_response)

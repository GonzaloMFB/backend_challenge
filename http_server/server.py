import socket

# HTTP Request:
# Line 0: Request line (e.g. GET /path HTTP/1.1)
# Line 1: Headers
# Line 2: -BLANK LINE- (separates headers from body)
# Line 3: Body (for requests like post)

# Define and bind socket
HOST = "127.0.0.1"  # localhost
PORT = 8080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as sock:
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
                conn.sendall(stream)

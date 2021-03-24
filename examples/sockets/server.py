import socket
import concurrent.futures


HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999


def handle_client(conn, addr):
    with conn:
        print(f'Connected from client:{addr}')
        while True:
            msg = conn.recv(1024)
            if not msg:
                print(f'Connection closed from {addr}')
                break
            print(f'Received: {msg.decode()}')
            conn.sendall('Hi from server'.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f'Server is listening at {HOST}:{PORT}')
    while True:
        conn, addr = server.accept()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(handle_client, conn, addr)

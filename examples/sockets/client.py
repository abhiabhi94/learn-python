import socket


HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    client.sendall('Hi'.encode())
    data = client.recv(1024)
    print(f'Received from the server: {data.decode()}')

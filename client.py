from socket import create_connection


def create_client_socket():
    with create_connection(('localhost', 8080)) as sock:
        while True:
            sock.send(bytes(input(': ').encode()))
            data = sock.recv(1024)
            print(f'out: {data.decode()}')


create_client_socket()
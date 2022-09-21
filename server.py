from socket import create_server


def server_socket():
    with create_server(('localhost', 8080), backlog=1) as sock:
        while True:
            connection, client_adress = sock.accept()
            print(f'Подключение пользователя: {client_adress}')
            while True:
                data = connection.recv(1024)
                if data:
                    print(f'in: {data.decode()}')
                    connection.sendall(input('out: ').encode())
                else:
                    break
            connection.close()
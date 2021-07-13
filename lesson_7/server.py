from socket import socket, AF_INET, SOCK_STREAM
import select


def write_response(message, w_clients, clients):
    for sock in w_clients:
        try:
            sock.send(message.encode('utf-8'))
        except:
            sock.close()
            clients.remove(sock)


def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', 9999))
    sock.listen(5)
    sock.settimeout(2)

    clients = []

    while True:
        try:
            conn, addr = sock.accept()
            print('Получение соединение от: ', addr)
        except OSError:
            pass
        else:
            clients.append(conn)
        finally:
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], 0)
            except:
                pass

            for client in r:
                try:
                    message = client.recv(1024).decode('utf-8')
                    print('message: ', message)
                    write_response(message, w, clients)
                except:
                    clients.remove(client)


if __name__ == '__main__':
    main()

def read_message(socket):
    response = socket.recv(1024)
    return response.decode('utf-8')

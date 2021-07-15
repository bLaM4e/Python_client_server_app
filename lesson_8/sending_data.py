def write_message(socket):
    message = input('Enter your message: ')
    socket.send(message.encode('utf-8'))

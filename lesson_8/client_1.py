from socket import socket, AF_INET, SOCK_STREAM
from sending_data import write_message
from receiving_data import read_message

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 9999))

while True:
    write_message(s)
    print(read_message(s))

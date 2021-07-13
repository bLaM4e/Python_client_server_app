from socket import socket, AF_INET, SOCK_STREAM
from receiving_data import read_message

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 9999))

while True:
    print(read_message(s))

from socket import *
from config import codes, val_def
from utils import set_def_port_and_ip, is_valid_port_and_ip
import sys
import time
import json


def create_message(msg):
    time_str = time.ctime(time.time())
    if msg['action'] == 'presence':
        return {
            "response": 200,
            "time": time_str,
            "alert": codes[200]
        }
    else:
        return {
            "response": 400,
            "time": time_str,
            "error": codes[400]
        }


def main():
    port, ip = set_def_port_and_ip()
    data = sys.argv
    if '-p' in data:
        port = int(data[data.index('-p') + 1])
    if '-a' in data:
        ip = data[data.index('-a') + 1]

    is_val = is_valid_port_and_ip(port, ip)
    if not is_val:
        port, ip = set_def_port_and_ip()

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((ip, port))
    s.listen(val_def['MAX_CONNECTIONS'])

    while True:
        client, addr = s.accept()

        msg_from_client = json.loads(client.recv(val_def['MAX_PACKAGE_LENGTH']).decode(val_def['ENCODING']))
        msg_to_client = create_message(msg_from_client)

        response = json.dumps(msg_to_client)
        client.send(response.encode(val_def['ENCODING']))

        client.close()


if __name__ == '__main__':
    main()

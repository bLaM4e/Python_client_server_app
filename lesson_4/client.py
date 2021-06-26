from socket import *
from config import val_def
from utils import set_def_port_and_ip, is_valid_port_and_ip
import sys
import time
import json


def create_message():
    time_str = time.ctime(time.time())
    msg_presence = {
            "action": "presence",
            "time": time_str,
    }
    return msg_presence


def main():
    try:
        port, ip = int(sys.argv[2]), sys.argv[1]
        is_val = is_valid_port_and_ip(port, ip)
        if not is_val:
            port, ip = set_def_port_and_ip()
    except IndexError:
        port, ip = set_def_port_and_ip()

    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((ip, port))
    except ConnectionRefusedError:
        print('Неверно указаны порт или адрес сервера')
        sys.exit(1)

    msg = create_message()
    msg_to_server = json.dumps(msg)
    s.send(msg_to_server.encode(val_def['ENCODING']))

    response = json.loads(s.recv(val_def['MAX_PACKAGE_LENGTH']).decode(val_def['ENCODING']))
    if response.get('alert'):
        print(f'Код ответа {response["response"]} - {response["alert"]}')
    else:
        print(f'Код ответа {response["response"]} - {response["error"]}')

    s.close()


if __name__ == '__main__':
    main()

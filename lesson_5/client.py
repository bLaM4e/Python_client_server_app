from socket import *
from config import val_def
from utils import set_def_port_and_ip, is_valid_port_and_ip
from log.client_log_config import log_client
import sys
import time
import json


def create_message():
    time_str = time.ctime(time.time())
    msg_presence = {
            "action": "presence",
            "time": time_str,
    }
    log_client.info('Создано presence-сообщение')
    return msg_presence


def main():
    try:
        port, ip = int(sys.argv[2]), sys.argv[1]
        is_val = is_valid_port_and_ip(port, ip)
        if not is_val:
            log_client.warning('Допущена ошибка в написание ip-адреса или порта')
            port, ip = set_def_port_and_ip()
    except IndexError:
        log_client.error('Не был указан порт или ip')
        port, ip = set_def_port_and_ip()

    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((ip, port))
    except ConnectionRefusedError:
        log_client.error(f'Не существует сервера с адресом {ip}:{port}')
        sys.exit(1)

    msg = create_message()
    msg_to_server = json.dumps(msg)
    s.send(msg_to_server.encode(val_def['ENCODING']))
    log_client.info('Отправлено presence-сообщение')

    response = json.loads(s.recv(val_def['MAX_PACKAGE_LENGTH']).decode(val_def['ENCODING']))
    if response.get('alert'):
        log_client.info(f'Получен ответ от сервера {response["response"]} - {response["alert"]}')
    else:
        log_client.info(f'Получен ответ от сервера {response["response"]} - {response["error"]}')

    s.close()


if __name__ == '__main__':
    main()

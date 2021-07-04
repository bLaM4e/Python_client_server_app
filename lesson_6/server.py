from socket import *
from config import codes, val_def
from utils import set_def_port_and_ip, is_valid_port_and_ip
from decorators.log_server import Log
import sys
import time
import json
from log.server_log_config import log_server


@Log()
def create_message(msg):
    time_str = time.ctime(time.time())
    if msg['action'] == 'presence':
        log_server.info('Создпно сообщение клиенту(код 200)')
        return {
            "response": 200,
            "time": time_str,
            "alert": codes[200]
        }
    else:
        log_server.warning('Создано сообщение клиенту(код 400)')
        return {
            "response": 400,
            "time": time_str,
            "error": codes[400]
        }


@Log()
def main():
    data = sys.argv
    try:
        if '-p' in data:
            port = int(data[data.index('-p') + 1])
        else:
            port = val_def['DEFAULT_PORT']
            log_server.warning(f'Был задан порт по умолчанию {port}')
    except IndexError:
        log_server.critical('После -"р" не указан порт')
        sys.exit(1)
    except ValueError:
        log_server.critical(f'После -"р" не указан порт -- {data}')
        sys.exit(1)

    try:
        if '-a' in data:
            ip = data[data.index('-a') + 1]
        else:
            ip = val_def['DEFAULT_IP_ADDRESS']
            log_server.warning(f'Был задан ip-адрес по умолчанию {ip}')
    except IndexError:
        log_server.critical('После -"р" не указан порт')
        sys.exit(1)

    is_val = is_valid_port_and_ip(port, ip)
    if not is_val:
        log_server.warning('Допущена ошибка в написание ip-адреса или порта')
        port, ip = set_def_port_and_ip()

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((ip, port))
    s.listen(val_def['MAX_CONNECTIONS'])

    while True:
        client, addr = s.accept()

        msg_from_client = json.loads(client.recv(val_def['MAX_PACKAGE_LENGTH']).decode(val_def['ENCODING']))
        log_server.info('Получено сообщение от клиента')
        msg_to_client = create_message(msg_from_client)

        response = json.dumps(msg_to_client)
        client.send(response.encode(val_def['ENCODING']))
        log_server.info('Сообщение клиенту отправлено')

        client.close()


if __name__ == '__main__':
    main()

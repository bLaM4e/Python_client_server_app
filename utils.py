from config import val_def
import sys
import re


def set_def_port_and_ip():
    return val_def['DEFAULT_PORT'], val_def['DEFAULT_IP_ADDRESS']


def is_valid_port_and_ip(port, ip):
    try:
        validate_server_address = re.fullmatch(r'(\d{1,3}\.){3}\d{1,3}', ip)
        if not validate_server_address:
            raise SyntaxError
        if not 65535 >= port >= 1024:
            raise ValueError
    except ValueError:
        print('Порт должен быть указан в диапазоне от 1024 до 65535, был задан порт по умолчанию.')
        return False
    except SyntaxError:
        print('Вы допустили ошибку в написание ip-адреса, был задан IP по умолчанию.')
        return False
    return True

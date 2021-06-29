from config import val_def
from log.client_log_config import log_client


def set_def_port_and_ip():
    log_client.warning('Был задан ip и порт по умолчанию')
    return val_def['DEFAULT_PORT'], val_def['DEFAULT_IP_ADDRESS']


def is_valid_port_and_ip(port, ip):
    try:
        is_valid_ip = all(0 <= int(p) < 256 for p in ip.split('.'))
        if not is_valid_ip:
            raise ValueError
        if not 65535 >= port >= 1024:
            raise ValueError
    except ValueError:
        return False
    return True

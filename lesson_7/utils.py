from config import val_def
from decorators.log_client import log
from decorators.log_server import Log
from log.client_log_config import log_client


@Log()
def set_def_port_and_ip():
    log_client.warning('Был задан ip и порт по умолчанию')
    return val_def['DEFAULT_PORT'], val_def['DEFAULT_IP_ADDRESS']


@log
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

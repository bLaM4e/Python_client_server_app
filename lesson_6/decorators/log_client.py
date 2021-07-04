import sys
import inspect
import logging.handlers

sys.path.append('../ ')

log_d = logging.getLogger('decorator_logs_client')

log_d.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)-30s %(message)s')
log_handler = logging.handlers.TimedRotatingFileHandler('client.log', encoding='utf-8', interval=30, when='D')
log_handler.setFormatter(formatter)
log_d.addHandler(log_handler)


def log(func):
    def wrapper(*args, **kwargs):
        code_obj_name = inspect.currentframe().f_back.f_code.co_name
        if '<module>' != code_obj_name:
            log_d.info(f'Функция {func.__name__} вызвана из функции {code_obj_name}')
        log_d.info(f'function - {func.__name__} : args - {args} : kwargs - {kwargs}')
        return func(*args, **kwargs)
    return wrapper

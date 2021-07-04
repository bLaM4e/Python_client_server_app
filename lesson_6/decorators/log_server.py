import sys
import inspect
import logging.handlers

sys.path.append('../ ')

log = logging.getLogger('decorator_logs_client')

log.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)-30s %(message)s')
log_handler = logging.handlers.TimedRotatingFileHandler('server.log', encoding='utf-8', interval=30, when='D')
log_handler.setFormatter(formatter)
log.addHandler(log_handler)


class Log:
    def __init__(self):
        pass

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            code_obj_name = inspect.currentframe().f_back.f_code.co_name
            if code_obj_name != '<module>':
                log.info(f'Функция {func.__name__} вызвана из функции {code_obj_name}')
            log.info(f'function - {func.__name__} : args - {args} : kwargs - {kwargs}')
            return func(*args, **kwargs)
        return wrapper


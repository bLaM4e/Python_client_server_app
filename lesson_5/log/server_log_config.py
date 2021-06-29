import logging
import logging.handlers
import sys

sys.path.append('../ ')

log_server = logging.getLogger('server_log')

log_server.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelno)s %(name)s %(message)s')
# client_handler = logging.FileHandler('server.log')
client_handler = logging.handlers.TimedRotatingFileHandler('server.log', encoding='utf-8', interval=1, when='D')
client_handler.setFormatter(formatter)
log_server.addHandler(client_handler)
log_server.addHandler(logging.StreamHandler(sys.stderr))

# log_server.debug('debug message')
# log_server.info('info message')
# log_server.warning('warning message')
# log_server.error('error message')
# log_server.critical('critical message')

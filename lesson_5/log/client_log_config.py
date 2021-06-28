import logging
import sys

sys.path.append('../ ')

log_client = logging.getLogger('client_log')

log_client.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelno)s %(name)s %(message)s')
client_handler = logging.FileHandler('client.log')
client_handler.setFormatter(formatter)
log_client.addHandler(client_handler)
log_client.addHandler(logging.StreamHandler(sys.stderr))

# log_client.info('info message')

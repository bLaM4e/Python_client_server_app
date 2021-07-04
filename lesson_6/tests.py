import unittest
import time
from config import codes
from server import create_message as create_message_server
from client import create_message as create_message_client
from utils import set_def_port_and_ip, is_valid_port_and_ip


class TestServer(unittest.TestCase):
    time_str = time.ctime(time.time())
    msg_from_client_alert = {"action": "presence", "time": "Thu Jun 24 13:55:52 2021"}
    msg_from_client_error = {"action": "prоbe", "time": "Thu Jun 24 13:55:52 2021"}

    def test_create_message_server_alert(self):
        self.assertEqual(create_message_server(self.msg_from_client_alert), {"response": 200,
                                                                             "time": self.time_str,
                                                                             "alert": codes[200]})

    def test_create_message_server_error(self):
        self.assertEqual(create_message_server(self.msg_from_client_error), {"response": 400,
                                                                             "time": self.time_str,
                                                                             "error": codes[400]
                                                                             })

    def test_create_message_client_error(self):
        self.assertEqual(create_message_client(), {"action": "presence",
                                                   "time": self.time_str,
                                                   })

    def test_set_def_port_and_ip(self):
        self.assertEqual(set_def_port_and_ip(), (7777, '127.0.0.1'))

    def test_is_valid_port(self):
        self.assert_(is_valid_port_and_ip(1025, '10.10.255.255'))

    def test_is_valid_ip(self):
        self.assert_(is_valid_port_and_ip(1025, '100.100.10.10'))


if __name__ == '__main__':
    unittest.main()

import socket
import json

from config.constants import *

class Connection:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

    def connect(self, name):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.host, self.port))

        self.send(HANDSHAKE, name)

        packet = self.receive()

        if packet["type"] == FAILED:
            return False

        return True

    def disconnect(self):
        self.connection.close()

    def send(self, type, payload=None):
        packet = {"type":type, "payload":payload}
        self.connection.send(json.dumps(packet).encode())

    def receive(self):
        packet = self.connection.recv(1024).decode()
        packet = json.loads(packet)

        return packet

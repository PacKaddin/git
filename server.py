from threading import Thread
import socket
import json
from enum import IntEnum

SERVER = "0.0.0.0"
PORT = 8080
MLEN = 1000
QUEUE_LENGTH = 10

class Operacia(IntEnum):
    LOGIN = 1
    EXIT = 2
    USERS = 3

class Sprava:
    def __init__(self, paOd, paKomu, paOperacia, paText):
        self.od = paOd
        self.komu = paKomu
        self.operacia = paOperacia
        self.text = paText
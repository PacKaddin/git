from threading import Thread
import socket
import json
from enum import IntEnum

SERVER = "0.0.0.0"
PORT = 8080
MLEN = 1000
QUEUE_LENGTH = 10

class Operacia(intEnum):
    LOGIN = 1
    EXIT = 2
    USERS = 3
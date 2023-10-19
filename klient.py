import socket
import json
from enum import IntEnum

SERVER = "127.0.0.1"
PORT = 8080

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

    @staticmethod
    def json_decoder(paObj):
        return Sprava(paObj['od'], paObj['komu'], paObj['operacia'], paObj['text'])

def napoveda():
    print("NAPOVEDA:")
    print("    \q ukonci program")
    print("    \l vypise pouzivatelov")
    print("    \h help")
    print("    Spravu posielajte v tvare: prijemca:sprava")


print("CHAT KLIENT")
od = input("Zadaj meno")

napoveda()


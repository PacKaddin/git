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

    @staticmethod
    def json_decoder(paObj):
        return Sprava(paObj['od'], paObj['komu'], paObj['operacia'], paObj['text'])

def VybavKlienta(paClientSocket, paClientAddr, paPouzivatelia):

    while(True):
        sprava = paClientSocket.recv(MLEN)
        jsonStr = sprava.decode()
        message = json.loads(jsonStr, object_hook=Sprava.json_decoder)

        if message.operacia == Operacia.LOGIN:
            paPouzivatelia.append(message.od)
            print("Prihlasil sa {} z IP {}, port {}".format(message.od, paClientAddr[0], paClientAddr[1]))
            continue

        if message.operacia == Operacia.EXIT:
            paPouzivatelia.remove(message.od)
            print("Odhlasil sa {} z IP {}, port {}".format(message.od, paClientAddr[0], paClientAddr[1]))
            return

        if message.operacia == Operacia.USERS:
            odpoved = Sprava("SERVER", message.od, Operacia.USERS.value, paPouzivatelia)
            jsonStr = json.dumps(odpoved.__dict__)
            paClientSocket.send(jsonStr.encode())
            continue


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVER, PORT))
    sock.listen(QUEUE_LENGTH)

    pouzivatelia = list()

    print("Spustil sa server")

    while True:
        (clientSock, clientAddr) = sock.accept()
        t = Thread(target=VybavKlienta, args=(clientSock, clientAddr, pouzivatelia))
        t.start()
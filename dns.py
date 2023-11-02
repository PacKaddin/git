import socket
import struct
import ipaddress

DNS_SERVER = "1.1.1.3"
DNS_PORT = 80
BIND_PORT = 52586

# HEADER
transaction_id = 0x1231
flags = 0x0100
questions = 0x0001
answers = 0x0000
authority = 0x0000
additional = 0x0000

header = struct.pack()
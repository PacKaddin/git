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

header = struct.pack('!6H', transaction_id, flags, questions, answers, authority, additional)


question = "www.uniza.sk"
labels = question.split('.')

query_body = b''

for label in labels:
    query_body += bytes([len(label)])

    for char in label:
        query_body += bytes([ord(char)])
query_body += bytes([0x00])


query_type = 0x0001
query_class = 0x0001

query_end = struct.pack('!2h', query_type, query_class)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind(('0.0.0.0', BIND_PORT))
except:
    print('Error in bind')
    exit(1)

sock.sendto(header + query_body + query_end, (DNS_SERVER, DNS_PORT))




import socket

HEADER = 64
PORT = 5000
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.1.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

def send(msg):
    message = msg.encode(FORMAT)
    msg_header = str(len(message)).encode(FORMAT)
    msg_header += b' ' * (HEADER - len(msg_header))
    client.send(msg_header)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello!")
input()
send("Goodbye!")
input()
send("!DISCONNECT")

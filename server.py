import socket
import threading

HEADER = 64
PORT = 5000
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

def handle_client(sock, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_len = sock.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = sock.recv(msg_len).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            sock.send("Msg received".encode(FORMAT))

    sock.close()

def main():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        sock, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(sock, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")


print("[STARTING] server is starting...")
main()

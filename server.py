import socket
import os
import sys
from threading import Thread

SERVER_PORT = 0
needtoquit = False

def sayerror():
    print("An error has occurred! xTerminal cannot continue!")
    sys.exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

print("        _____ _           _       _____                          ")
print("       / ____| |         | |     / ____|                         ")
print(" __  _| |    | |__   __ _| |_   | (___   ___ _ ____   _____ _ __ ")
print(" \ \/ / |    | '_ \ / _` | __|   \___ \ / _ \ '__\ \ / / _ \ '__|")
print("  >  <| |____| | | | (_| | |_    ____) |  __/ |   \ V /  __/ |   ")
print(" /_/\_\\\_____|_| |_|\__,_|\__|  |_____/ \___|_|    \_/ \___|_|   \n")

SERVER_HOST = "0.0.0.0"
try:
    SERVER_PORT = int(input("Port: "))
except:
    sayerror()

separator_token = "<SEP>"

try:
    client_sockets = set()
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print("[*] Listening as "+SERVER_HOST+":"+str(SERVER_PORT))
except Exception as e:
    sayerror()

def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            pass
            print("[!] Server error! Disconnecting user!")
            for cs in client_sockets:
                cs.close()
            needtoquit = True
            break
        else:
            msg = msg.replace(separator_token, ": ")
        for client_socket in client_sockets:
            try:
                client_socket.send(msg.encode())
            except:
                pass


while True:
    if needtoquit == True:
        break
    client_socket, client_address = s.accept()
    print("[+] "+str(client_address)+" connected.")
    client_sockets.add(client_socket)
    try:
        t = Thread(target=listen_for_client, args=(client_socket,))
        t.daemon = True
        t.start()
    except:
        pass

for cs in client_sockets:
    if needtoquit == True:
        break
    cs.close()
s.close()
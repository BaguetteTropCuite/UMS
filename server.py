import socket

HOST = "10.0.100.100"
PORT = 55000


serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serveur.connect((HOST,PORT))

msg = serveur.recv(1024)
print(msg.decode("utf-8"))
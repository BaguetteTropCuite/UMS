import socket


"""
Création d'une connection TCP/IP vers le serveur de monitoring

"""


HOST = "10.0.100.100"    # <=== Adresse IP du serveur
PORT = 65432             # <=== Port utilisé par le serveur (peut être changé des deux cotés)


#Connection au serveur : 
with socket.socket(socket.AF_INET, socket.SOCK) as s:  # <=== AF_INET pour IPV4 sockstreal pour tcp
    s.connet((HOST, PORT))
    s.sendall(b"test")
    data = s.recv(1024)

print(f"Recu : {data!r}")
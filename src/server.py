"""
La fonction ci-dessus va envoyer les données collecter sur le monitoring au server de monitoring.


====== A EDITER ET A ADAPTER ===========================
|                                                      |
|    HOST = STR     <== IP du serveur                  |
|    PORT = INT     <== Port du serveur (defaut 55000) |
|                                                      |
========================================================

"""

import socket
import json

HOST = "10.0.100.100"       #IP_DE_VOTRE_SERVEUR
PORT = 55000                #PORT defaut 55000



def envoyer_data(cpu_usage,ram_usage,disque_usage):



    """
    Les données sont envoyé en respectant le format json
    """


    message = {
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "disque_usage": disque_usage
    }


    # CONNECTION AU SERVEUR : 

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:

            serveur.connect((HOST,PORT))                                                            # Connection au serveur
            message_json = json.dumps(message)                                                      # Converti le dictionnaire message au format json dans la variable "message_json"
            serveur.sendall(message_json.encode('utf-8'))                                                # Les données sont envoyé au serveur

    except Exception as erreur:

        print(f"""
        
        UNE ERREUR S'EST PRODUITE LORS DE L'ENVOIE DES DONNEES AU SERVEUR, VERIFIER : 

        La definition de la variable HOST et PORT dans le fichier server.py
        La configuration du serveur (fichier server.py)
        
        {erreur}

        """)


#envoyer_data(12,44,80)          UTILISE POUR TEST

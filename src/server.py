"""
La fonction ci-dessus va envoyer les données collectées sur le monitoring au server de monitoring.


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



def envoyer_data(cpu_usage, ram_used, ram_total, disque_used, disque_total, reseau_upload, reseau_download):



    """
    Les données sont envoyées en respectant le format json
    """


    message = {
        "cpu_usage": cpu_usage,
        "ram_used": ram_used,
        "ram_total": ram_total,
        "disque_used": disque_used,
        "disque_total": disque_total,
        "reseau_upload": reseau_upload,
        "reseau_download": reseau_download
    }


    # CONNECTION AU SERVEUR : 

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:   # <= IPV4 + TCP

            serveur.connect((HOST,PORT))                                                            # Connexion au serveur
            message_json = json.dumps(message)                                                      # Converti le dictionnaire message au format json dans la variable "message_json"
            serveur.sendall(message_json.encode('utf-8'))                                                # Les données sont envoyées au serveur

    except Exception as erreur:

        print(f"""
        
        UNE ERREUR S'EST PRODUITE LORS DE L'ENVOIE DES DONNEES AU SERVEUR, VERIFIER : 

        La definition de la variable HOST et PORT dans le fichier server.py
        La configuration du serveur (fichier server.py)
        
        {erreur}

        """)


#envoyer_data(12,44,80)          UTILISE POUR TEST

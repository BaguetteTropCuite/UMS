from psutil import cpu_percent, disk_usage, virtual_memory, net_io_counters
from statistics import mean
import os, socket, platform, time






"""
    La classe hote à pour but de ramener les informations de base au bon fonctionnement de l'application.

    La classe Monitoring (qui hérite de hote) à pour but d'établir toutes les fonctionnalitées du système de monitoring

    L'objectif de cette architecture est la lisibilité et la possibilité de l'intégration des nouvelles fonctionnalitées

"""


class Hote:                                          # <=== Classe parent du système de monitoring  objectif : (Info systeme (distribution, ip, version paquet ect ...))
    def __init__(self):
        self.systeme_os = platform.system()          # <=== Version du système d'exploitation, retourne Linux pour l'instant (Implémenter une fonction pour trouver la version exacte)


    def host_version(self):                          # <=== Si besoin d'afficher la version systeme
        return self.systeme_os



class Monitoring(Hote):                              # <=== Classe pour le système de monitoring, objectif : (RAM, CPU, Réseau, Disque)

    def __init__(self,network_interface_name):
        super().__init__()
        #nom de la carte réseau
        self.network_interface_name = network_interface_name
        #RAM en mb
        self._ram_used = None
        self._ram_total = None
        #CPU en %                                  
        self._avg_cpu = None
        #Disque en mb                          
        self._disque_used = None
        self._disque_total = None
        #Reseau
        self._reseau_upload = None
        self._reseau_download = None
        


    def utilisation_cpu(self):                       # <=== Retourne l'usage du CPU moyen sur une minute de monitoring. Retourne un float
         
        self._avg_cpu = cpu_percent(interval=1)               #Bloque l'execution pour mesurer l'usage moyen sur l'interval

        return self._avg_cpu



    def utilisation_memoire(self):                   # <=== memoire_pourcent = float, memoire_used & memoire_total = int
        """
            Retourne 3 valeurs : 
                en mb memoire_used = mémoire actuellement utilisé par le système
                en mb memoire_total = mémoire disponible sur l'hote
                memoire_pourcent = Utilisation de la mémoire en pourcentage

        """
        
        memoire = virtual_memory()

        self._ram_used = memoire.used // (1024 ** 2)
        self._ram_total = memoire.total // (1024 ** 2)

        #memoire_pourcent = memoire.percent             #Utiliser pour le debug, calcul coté serveur avec les valeurs max et used

        #return self._ram_used, self._ram_total

    
    def utilisation_disque(self):                    # <=== Retourne à l'instant T le pourcentage d'utilisation du disk HDD les valeurs retourné sont en INT

        disque = disk_usage('/')

        self._disque_used = disque.used >> 20 #mb
        self._disque_total = disque.total >> 20 #mb

        #disque_percent = disque.percent             # debug

        #return self._disque_used, self._disque_total

    def utilisation_reseau(self,):                  # <=== Retourne deux INT

        interface_stat_debut = net_io_counters(pernic=True, nowrap=True)[self.network_interface_name]
        time_debut = time.time()

        time.sleep(1)

        interface_stat_fin = net_io_counters(pernic=True, nowrap=True)[self.network_interface_name]
        time_fin = time.time()

        self._reseau_upload = interface_stat_fin.bytes_sent - interface_stat_debut.bytes_sent
        self._reseau_download = interface_stat_fin.bytes_recv - interface_stat_debut.bytes_recv



        return self._reseau_upload, self._reseau_download   # renvoie le nombre de byte envoyé en une seconde, ainsi que le nombre de byte recu dans cette seconde





    def utilisation_avg(self):     #???
        
        return self._avg_cpu, self._ram_used, self._ram_total, self._disque_used, self._disque_total, self._reseau_upload, self._reseau_download

    
    def retour_avg(self):         # ???
        avg_cpu = mean(self._avg_cpu)
        avg_ram = mean(self._avg_ram)

        return avg_cpu, avg_ram, self._disque








"""
==========
TEST UNIT
==========


client = Monitoring(network_interface_name="enp1s0f0u4")

#print(client.host_version())
#print(client.utilisation_cpu())
#print(client.utilisation_memoire())
#print(client.utilisation_disque())
c_value = client.utilisation_cpu()
m_value_u, m_value_m = client.utilisation_memoire()
d_value_u, d_value_m = client.utilisation_disque()
up, down = client.utilisation_reseau()
"""

#print(f"""cpu usage : {c_value} %""")

#print(f"""value = {type(m_value_u)}/{m_value_m}""")

#print(f"""value = {d_value_u}/{d_value_m}""")       

#print(f""" UP : {type(up)} down : {down}""")

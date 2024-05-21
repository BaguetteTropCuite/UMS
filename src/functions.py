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
        self._ram_used = []
        self._ram_total = []
        #CPU en %                                  
        self._avg_cpu = [] 
        #Disque en mb                          
        self._disque_used = []
        self._disque_total = []
        #Reseau
        self._reseau_upload = []
        self._reseau_download = []
        


    def utilisation_cpu(self):                       # <=== Retourne à l'instant T le pourcentage d'utilisation du CPU (all core)
        return cpu_percent(interval=0.5) 



    def utilisation_memoire(self):                   # <=== memoire_pourcent = float, memoire_used & memoire_total = int
        """
            Retourne 3 valeurs : 
                en mb memoire_used = mémoire actuellement utilisé par le système
                en mb memoire_total = mémoire disponible sur l'hote
                memoire_pourcent = Utilisation de la mémoire en pourcentage

        """
        
        memoire = virtual_memory()

        memoire_used = memoire.used // (1024 ** 2)      # // (1024 * 1024) pour mb | // (1024 * 1024 * 1024) pour gb
        memoire_total = memoire.total // (1024 ** 2)
        #memoire_pourcent = memoire.percent             #Utiliser pour le debug, calcul coté serveur avec les valeurs max et used

        return memoire_used, memoire_total

    
    def utilisation_disque(self):                    # <=== Retourne à l'instant T le pourcentage d'utilisation du disk HDD

        disque = disk_usage('/')

        disque_used = disque.used >> 20 #mb
        disque_total = disque.total >> 20 #mb
        #disque_percent = disque.percent             # debug

        return disque_used, disque_total

    def utilisation_reseau(self,):
        interface_stat_debut = net_io_counters(pernic=True, nowrap=True)[self.network_interface_name]
        time_debut = time.time()

        time.sleep(1)

        interface_stat_fin = net_io_counters(pernic=True, nowrap=True)[self.network_interface_name]
        time_fin = time.time()

        upload = interface_stat_fin.bytes_sent - interface_stat_debut.bytes_sent
        download = interface_stat_fin.bytes_recv - interface_stat_debut.bytes_recv



        return upload, download   # renvoie le nombre de byte envoyé en une seconde, ainsi que le nombre de byte recu dans cette seconde





    def utilisation_avg(self):     #???

        m = Monitoring()

        self._avg_cpu.append(m.utilisation_cpu())
        self._avg_ram.append(m.utilisation_memoire())
        self._disque = m.utilisation_disque()             # <=== Pas du tout opti à changer 

    
    def retour_avg(self):         # ???
        avg_cpu = mean(self._avg_cpu)
        avg_ram = mean(self._avg_ram)

        return avg_cpu, avg_ram, self._disque








"""
==========
TEST UNIT
==========
"""

client = Monitoring(network_interface_name="enp1s0f0u4")

#print(client.host_version())
#print(client.utilisation_cpu())
#print(client.utilisation_memoire())
#print(client.utilisation_disque())
c_value = client.utilisation_cpu()
m_value_u, m_value_m = client.utilisation_memoire()
d_value_u, d_value_m = client.utilisation_disque()
up, down = client.utilisation_reseau()

print(f"""cpu usage : {c_value} %""")

print(f"""value = {m_value_u}/{m_value_m}""")

print(f"""value = {d_value_u}/{d_value_m}""")       

print(f""" UP : {up} down : {down}""")

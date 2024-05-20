from psutil import cpu_percent, disk_usage, virtual_memory
from statistics import mean
import os, socket, platform






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

    def __init__(self):
        super().__init__()
        self._avg_ram = []                           #<=\
        self._avg_cpu = []                           #<=== Variable qui stock les données toutes les 2 secondes pour le calcul de l'AVG
        self._disque = []                            #<=/
        self._avg_reseau = []
        


    def utilisation_cpu(self):                       # <=== Retourne à l'instant T le pourcentage d'utilisation du CPU
        return cpu_percent(interval=0.2)



    def utilisation_memoire(self):                   # <=== Retourne à l'instant T le pourcentage d'utilisation de la mémoire vive
        
        memoire = virtual_memory()

        memoire_pourcent = memoire.percent

        return memoire_pourcent

    
    def utilisation_disque(self):                    # <=== Retourne à l'instant T le pourcentage d'utilisation du disk HDD

        disque = disk_usage('/')

        disque_pourcent = disque.percent

        return disque_pourcent


    def utilisation_avg(self):

        m = Monitoring()

        self._avg_cpu.append(m.utilisation_cpu())
        self._avg_ram.append(m.utilisation_memoire())
        self._disque = m.utilisation_disque()             # <=== Pas du tout opti à changer 

    
    def retour_avg(self):
        avg_cpu = mean(self._avg_cpu)
        avg_ram = mean(self._avg_ram)

        return avg_cpu, avg_ram, self._disque








"""
==========
TEST UNIT
==========

client = Monitoring()

print(client.host_version())

print(client.utilisation_cpu())
print(client.utilisation_memoire())
print(client.utilisation_disque())
"""
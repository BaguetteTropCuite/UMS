
"""
    Déclaration des variables global c'est variables seront incrémenté par la fonction avg_info
"""
_avg_ram = []       # <=== Valeur moyenne de l'usage RAM en % (Valeur ajouter toutes les secondes pendant 1 MN)
_avg_cpu = []       # <=== Valeur moyenne de l'usage cpu en % (Valeur ajouter toutes les secondes pendant 1 MN)
_disk = None        # <=== Valeur pourcentage d'usage du disque dur




"""
    Fonctions de récupération des valeurs CPU, RAM, DISK à l'aide de psutil
"""


from psutil import cpu_percent, disk_usage, virtual_memory        #Utilisation pour afficher les utilisations systèmes
from statistics import mean                                       #Pour calculer les AVG sur les lists func acg_affichage



def info_cpu():
    return cpu_percent(interval=0.5)                                     # <=== Retourne à l'instant T le pourcentage d'utilisation du CPU
    #return psutil.cpu_percent(interval=0.5)




def info_memoire():                                 # <=== Retourne à l'instant T le pourcentage d'utilisation de la mémoire vive

    memory = virtual_memory()

    memory_pourcent = memory.percent

    return memory_pourcent



def info_disque():                                  # <=== Retourne à l'instant T le pourcentage d'utilisation du disk HDD
    disk = disk_usage('/')

    disk_pourcentage = disk.percent

    return disk_pourcentage



def avg_info(cpu,ram,disk):                         # <=== # Cette fonction retourne les 2 valeurs (AVG) du CPU RAM ainsi que l'etat du disque
    
    #CPU
    _avg_cpu.append(cpu)

    #RAM
    _avg_ram.append(ram)

    #Disk
    _disk = disk


def affichage_avg():                              # <=== Retourne dans trois variables les valeurs AVG

    avg_cpu = mean(_avg_cpu)      #Calcule l'utilisation moyenne puis la stock dans la variable avg_xxx avant d'être retourné
    avg_ram = mean(_avg_ram)

    return avg_cpu, avg_ram, _disk
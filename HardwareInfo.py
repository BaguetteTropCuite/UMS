
"""
    Déclaration des variables global
"""
_avg_ram = []       # <=== Valeur moyenne de l'usage RAM en % (Valeur ajouter toutes les secondes pendant 1 MN)
_avg_cpu = []       # <=== Valeur moyenne de l'usage cpu en % (Valeur ajouter toutes les secondes pendant 1 MN)
_disk = None        # <=== Valeur pourcentage d'usage du disque dur




"""
    Fonctions de récupération des valeurs CPU, RAM, DISK à l'aide de psutil
"""


from psutil import cpu_percent, disk_usage, virtual_memory



def info_cpu():                                     # <=== Retourne à l'instant T le pourcentage d'utilisation du CPU
    return psutil.cpu_percent(interval=0.5)




def info_memoire():                                 # <=== Retourne à l'instant T le pourcentage d'utilisation de la mémoire vive

    memory = psutil.virtual_memory()

    memory_pourcent = memory.percent

    return memory_pourcent



def info_disque():                                  # <=== Retourne à l'instant T le pourcentage d'utilisation du disk HDD
    disk = psutil.disk_usage('/')

    disk_pourcentage = disk.percent

    return disk_pourcentage



def avg_info(cpu,ram,disk):                         # <=== # Cette fonction retourne les 2 valeurs (AVG) du CPU RAM ainsi que l'etat du disque
    
    #CPU
    _avg_cpu.append(cpu)

    #RAM
    _avg_ram.append(ram)

    #Disk
    _disk = disk


def affichage_avg():                                # <=== Retourne dans trois variables les valeurs AVG
    return _avg_cpu, _avg_ram, _disk




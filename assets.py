import psutil


#Retourne chaque seconde le pourcentage d'utilisation du CPU
def CpuInfo():
    return psutil.cpu_percent(interval=1)



#Retourne chaque seconde des info sur la mémoire
def MemoryInfo():

    memory = psutil.virtual_memory()

    memory_pourcent = memory.percent

    return memory_pourcent

#Retourne l'esapace disque disponible en pourcentage
def DiskInfo():
    disk = psutil.disk_usage('/')

    disk_pourcentage = disk.percent

    return disk_pourcentage
    

from HardwareInfo import info_cpu, info_disque, info_memoire, avg_info, affichage_avg
import time
import os


x = 0

while True:

    avg_info(info_cpu(),info_memoire(),info_disque())


    print(f"CPU usage    : {info_cpu()} %")
    print(f"RAM usage    : {info_memoire()} %")
    print(f"DISQUE usage : {info_disque()} %")
    print(x)

    time.sleep(0.1)

    os.system('clear')

    x += 1

    if (x == 60):
        #Fonction envoie code au serveur

        cpu, ram, disk = affichage_avg()           # La fonction retourne 3 valeurs, qui doivent être stocké dans une variable avant d'être lu

        print(f"""
        CPU    : {info_cpu()} %
        Ram    : {info_memoire()} % 
        Disque : {info_disque()} %

        AVG CPU : {cpu} %
        AVG RAM : {ram} %
        """)

        break
    
        #x = 0       # <=== Reset X







    




    












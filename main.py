from HardwareInfo import info_cpu, info_disque, info_memoire, avg_info, affichage_avg
import time
import os

x = 0

while True:

    avg_info(info_cpu,info_memoire,info_disque)
    time.sleep(1)

    print(f"CPU usage : {info_cpu} %")
    print(f"CPU usage : {info_cpu} %")
    print(f"CPU usage : {info_cpu} %")
    os.system('clear')

    x+= 1

    if (x == 60):
        #Fonction envoie code au serveur

        cpu, ram, disk = affichage_avg()

        print("""
        CPU : {info_cpu} %              A finir 

        """)


        

        x = 0       # <=== Reset X







    




    












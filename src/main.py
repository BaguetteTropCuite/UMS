from functions import Hote, Monitoring     #Librairie de monitoring
import time
import os


x = 0

while True:

    x += 1

    m = Monitoring()

    if True:      # <== Changer True par False pour ne pas avoir d'affichage CLI dans le terminal du client (utile pour le debug)

        print(f"""

        CPU USAGE   : {m.utilisation_cpu()} %
        RAM Usage   : {m.utilisation_memoire()} %
        Disque Uage : {m.utilisation_disque()} %
        
        """)
        #time.sleep(2)
        #os.system('clear')

    if True:     # <== Monitoring

        

        m.utilisation_avg()    #Incremente les valeurs avg à chaque itération
        print(x)
        #time.sleep(2)
        os.system('clear')

        if (x == 60):
            
            cpu, ram, disque = m.retour_avg()

            #fonction envoie des données vers le serveur à l'aide des trois variables

            print(f"""

                CPU USAGE  AVG   : {cpu} %
                RAM Usage  AVG   : {ram} %
                Disque Uage AVG  : {disque} %
        
            """)
            
            break






        








    




    












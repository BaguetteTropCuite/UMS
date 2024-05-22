from functions import Hote, Monitoring     #Librairie de monitoring
import time
import os
import server
import multiprocessing

"""
    Changer le nom de la carte dans l'instance de la monitoring

"""

while True:

    monitoring = Monitoring(network_interface_name = "enp1s0f0u4")


    p1 = multiprocessing.Process(target=monitoring.utilisation_cpu, args=(monitoring,))
    p2 = multiprocessing.Process(target=monitoring.utilisation_reseau, args=(monitoring,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    

    monitoring.utilisation_memoire()
    monitoring.utilisation_disque()

    avg_cpu, ram_used, ram_total, disque_used, disque_total, reseau_upload, reseau_download = monitoring.utilisation_avg()

    #server.envoyer_data(avg_cpu, ram_used, ram_total, disque_used, disque_total, reseau_upload, reseau_download)

    print(f"""
            cpu = {avg_cpu} %
            ram = {ram_used}/{ram_total} mb
            disque = {disque_used}/{disque_total} mb
            reseau = {reseau_upload} UP  | {reseau_download} DOWN
    
    """)







        








    




    












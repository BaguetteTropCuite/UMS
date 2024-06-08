from functions import Hote, Monitoring  # Librairie de monitoring
import multiprocessing
from server import envoyer_data

def utilisation_cpu(queue, monitoring):
    cpu_usage = monitoring.utilisation_cpu()
    queue.put(cpu_usage)

def utilisation_reseau(queue, monitoring):
    try:
        reseau_upload, reseau_download = monitoring.utilisation_reseau()
        queue.put((reseau_upload, reseau_download))
    except KeyError as e:
        print(f"Erreur : Interface réseau non trouvée - {e}")
        queue.put((0, 0))


# DATA COLLECTION 
_cpu = []
_ram_used = []
_disque_used = []
_reseau_up = []
_reseau_down = []
xxx = 0

def main():
    global xxx
    monitoring = Monitoring(network_interface_name="enp6s0")  # Remplacez par le nom correct de l'interface réseau

    # Boucle de monitoring
    while True:  # Remplacez `while True` par `for _ in range(10)` pour tester
        # Création des queues
        cpu_queue = multiprocessing.Queue()
        reseau_queue = multiprocessing.Queue()

        # Création des processus
        p1 = multiprocessing.Process(target=utilisation_cpu, args=(cpu_queue, monitoring))
        p2 = multiprocessing.Process(target=utilisation_reseau, args=(reseau_queue, monitoring))

        # Démarrage des processus
        p1.start()
        p2.start()

        # Attente de la fin des processus
        p1.join()
        p2.join()

        # Récupération des résultats
        avg_cpu = cpu_queue.get()
        reseau_upload, reseau_download = reseau_queue.get()

        monitoring.utilisation_memoire()
        monitoring.utilisation_disque()

        ram_used = monitoring._ram_used
        ram_total = monitoring._ram_total
        disque_used = monitoring._disque_used
        disque_total = monitoring._disque_total


        _ram_used.append(ram_used)
        _disque_used.append(disque_used)
        _cpu.append(avg_cpu)
        _reseau_up.append(reseau_upload)
        _reseau_down.append(reseau_download)
        xxx += 1
        print(xxx)

        if xxx == 60:
            cpu = sum(_cpu) / len(_cpu)
            ram_usedd = sum(_ram_used) / len(_ram_used)
            disque_usedd = sum(_disque_used) / len(_disque_used)
            reseau_up = sum(_reseau_up)
            reseau_down = sum(_reseau_down)

            print(f"""
                AVGGGGGG        

                cpu = {cpu} %
                ram = {ram_usedd}/{ram_total} MB
                disque = {disque_usedd}/{disque_total} MB
                reseau = {reseau_up} UP | {reseau_down} DOWN
            """)

            # server.envoyer_data(avg_cpu, ram_used, ram_total, disque_used, disque_total, reseau_upload, reseau_download)
            envoyer_data(cpu, ram_usedd, ram_total, disque_usedd, disque_total, reseau_up, reseau_down)
            xxx = 0

        print(f"""
                cpu = {avg_cpu} %
                ram = {ram_used}/{ram_total} MB
                disque = {disque_used}/{disque_total} MB
                reseau = {reseau_upload} UP | {reseau_download} DOWN
        """)



if __name__ == "__main__":
    main()
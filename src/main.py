from functions import Hote, Monitoring  # Librairie de monitoring
import multiprocessing

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

def main():
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

        # server.envoyer_data(avg_cpu, ram_used, ram_total, disque_used, disque_total, reseau_upload, reseau_download)

        print(f"""
                cpu = {avg_cpu} %
                ram = {ram_used}/{ram_total} MB
                disque = {disque_used}/{disque_total} MB
                reseau = {reseau_upload} UP | {reseau_download} DOWN
        """)

if __name__ == "__main__":
    main()
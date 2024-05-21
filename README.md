UMS PROJECT 

Le projet UMS pour Uncomplicated Monitoring System, est un système de monitoring des serveurs linux (prochainement Windows) qui a pour but de permettre le monitoring simplifié, à moindre ressource que ce soit du côté client ou du serveur.


Le projet sera découpé en trois, une partie cliente Linux, une partie cliente Windows ainsi qu'une partie serveur Linux.


Fonctionnement : 

Client :
  Le script client, récupéra les informations de monitoring de la machine sur laquelle il est exécuté. (CPU, RAM, Disque, Réseau, Version ect ...).

  Il stockera en local pendant 60 secondes les valeurs de monitoring avec un interval de cinq secondes, puis toutes les 6O secondes, il rentrera en communication avec le serveur pour lui transmettre.

Serveur :
  Le serveur récupère les informations envoyées par les clients, puis stock ces informations, à l'aide d'une interface WEB minimaliste, le serveur Web affiche les comptes-rendus des serveurs.

  Exemple affichage du côté du serveur : 
  
![Image_Project](https://github.com/BaguetteTropCuite/UMS/assets/70807468/31ccc04a-3943-4fbb-bd51-04d7372b2865)

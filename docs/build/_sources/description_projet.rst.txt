Description du projet
=====================

Python OC Lettings FR est une application web Django refactorisée en architecture modulaire.

Le projet est désormais organisé en trois applications Django distinctes :

- ``oc_lettings_site`` : configuration globale, page d’accueil et pages d’erreur personnalisées
- ``lettings`` : gestion des adresses et des locations
- ``profiles`` : gestion des profils utilisateurs

L’objectif principal du projet est d’améliorer la maintenabilité, la lisibilité,
la testabilité et la capacité de déploiement de l’application.
Déploiement:
===========

Le projet a été préparé pour un déploiement industrialisé.

Déploiement avec Docker:
-----------------------

L’application peut être conteneurisée grâce au fichier ``Dockerfile`` fourni
dans le projet.

Déploiement avec Render:
-----------------------

L’application a été déployée sur la plateforme Render en tant que service web.

Le déploiement repose sur :

- Gunicorn comme serveur WSGI
- WhiteNoise pour la gestion des fichiers statiques
- des variables d’environnement pour la configuration
- GitHub Actions pour l’intégration continue
- Docker Hub pour la publication de l’image Docker
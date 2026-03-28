Installation
============

Prérequis
---------

- Python 3.12
- pip
- un environnement virtuel Python

Étapes d’installation
---------------------

1. Cloner le dépôt :

   .. code-block:: bash

      git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
      cd Python-OC-Lettings-FR

2. Créer et activer un environnement virtuel :

   .. code-block:: bash

      python -m venv .venv
      .venv\Scripts\activate

3. Installer les dépendances :

   .. code-block:: bash

      pip install -r requirements.txt

4. Appliquer les migrations :

   .. code-block:: bash

      python manage.py migrate

5. Lancer le serveur de développement :

   .. code-block:: bash

      python manage.py runserver
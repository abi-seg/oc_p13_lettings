Modèles de base de données
==========================

Application ``lettings``
------------------------

Modèle ``Address``
~~~~~~~~~~~~~~~~~~

Champs :

- ``number``
- ``street``
- ``city``
- ``state``
- ``zip_code``
- ``country_iso_code``

Modèle ``Letting``
~~~~~~~~~~~~~~~~~~

Champs :

- ``title``
- ``address`` : relation ``OneToOneField`` vers ``Address``

Application ``profiles``
------------------------

Modèle ``Profile``
~~~~~~~~~~~~~~~~~~

Champs :

- ``user`` : relation ``OneToOneField`` vers le modèle utilisateur Django
- ``favorite_city``
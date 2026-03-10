from django.db import migrations


def transferer_donnees_lettings(apps, schema_editor):
    """Copy Address and Letting rows from oc_lettings_site to lettings app."""
    AncienneAdresse = apps.get_model("oc_lettings_site", "Address")
    AncienLetting = apps.get_model("oc_lettings_site", "Letting")
    NouvelleAdresse = apps.get_model("lettings", "Address")
    NouveauLetting = apps.get_model("lettings", "Letting")

    correspondance_adresses = {}

    for ancienne_adresse in AncienneAdresse.objects.all().order_by("id"):
        nouvelle_adresse = NouvelleAdresse.objects.create(
            number=ancienne_adresse.number,
            street=ancienne_adresse.street,
            city=ancienne_adresse.city,
            state=ancienne_adresse.state,
            zip_code=ancienne_adresse.zip_code,
            country_iso_code=ancienne_adresse.country_iso_code,
        )
        correspondance_adresses[ancienne_adresse.id] = nouvelle_adresse.id

    for ancien_letting in AncienLetting.objects.all().order_by("id"):
        id_nouvelle_adresse = correspondance_adresses[ancien_letting.address_id]
        NouveauLetting.objects.create(
            title=ancien_letting.title,
            address_id=id_nouvelle_adresse,
        )


def annuler_transfert_lettings(apps, schema_editor):
    """Reverse function intentionally left empty (no destructive rollback)."""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(transferer_donnees_lettings, annuler_transfert_lettings),
    ]

from django.db import migrations


def transferer_donnees_profiles(apps, schema_editor):
    """Copy Profile rows from oc_lettings_site to profiles app."""
    AncienProfile = apps.get_model("oc_lettings_site", "Profile")
    NouveauProfile = apps.get_model("profiles", "Profile")

    for ancien_profile in AncienProfile.objects.all().order_by("id"):
        NouveauProfile.objects.create(
            user_id=ancien_profile.user_id,
            favorite_city=ancien_profile.favorite_city,
        )


def annuler_transfert_profiles(apps, schema_editor):
    """Reverse function intentionally left empty (no destructive rollback)."""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(transferer_donnees_profiles, annuler_transfert_profiles),
    ]

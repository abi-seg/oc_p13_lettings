"""Tests for lettings application."""
import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.fixture
def adresse():
    """Create and return an Address instance for tests."""
    return Address.objects.create(
        number=1,
        street="Main Street",
        city="Testville",
        state="TS",
        zip_code=12345,
        country_iso_code="USA",

    )


@pytest.fixture
def location(adresse):
    """Create and return a Letting instance linked to adresse."""
    return Letting.objects.create(
        title="Super location de test",
        address=adresse,
    )


@pytest.mark.django_db
def test_modele_adresse_str(adresse):
    """__str__ of Address should return 'number street'."""
    assert str(adresse) == "1 Main Street"


@pytest.mark.django_db
def test_modele_letting_str(location):
    """__str__ of letting should return its title."""
    assert str(location) == "Super location de test"


@pytest.mark.django_db
def test_vue_lettings_index(client, location):
    """Index view should list lettings and use correct template."""
    url = reverse("lettings:index")
    reponse = client.get(url)

    assert reponse.status_code == 200
    assert "lettings/index.html" in [
        template.name for template in reponse.templates]
    assert b"Super location de test" in reponse.content


@pytest.mark.django_db
def test_vue_letting_detail(client, location):
    """Detail view should display the selected letting."""
    url = reverse("lettings:letting", kwargs={"letting_id": location.id})
    reponse = client.get(url)

    assert reponse.status_code == 200
    assert "lettings/letting.html" in [
        template.name for template in reponse.templates]
    assert b"Super location de test" in reponse.content
    assert b"Main Street" in reponse.content

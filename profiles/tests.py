# Fichier de tests pour l'application profiles.
"""Tests for profiles application."""

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile


@pytest.fixture
def utilisateur():
    """Create and return a User instance for tests."""
    return User.objects.create_user(username="johndoe", password="password123")


@pytest.fixture
def profil(utilisateur):
    """Create and return a Profile instance for tests."""
    return Profile.objects.create(
        user=utilisateur,
        favorite_city="Test City",
    )


@pytest.mark.django_db
def test_modele_profile_str(profil):
    """__str__ of Profile should return username."""
    assert str(profil) == "johndoe"


@pytest.mark.django_db
def test_vue_profiles_index(client, profil):
    """Index view should list profiles and use correct template."""
    url = reverse("profiles:index")
    reponse = client.get(url)

    assert reponse.status_code == 200
    assert "profiles/index.html" in [template.name for template in reponse.templates]
    assert b"johndoe" in reponse.content


@pytest.mark.django_db
def test_vue_profile_detail(client, profil):
    """Detail view should display the selected profile."""
    url = reverse("profiles:profile", kwargs={"username": profil.user.username})
    reponse = client.get(url)

    assert reponse.status_code == 200
    assert "profiles/profile.html" in [template.name for template in reponse.templates]
    assert b"johndoe" in reponse.content
    assert b"Test City" in reponse.content
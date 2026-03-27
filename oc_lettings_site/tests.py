"""Tests for oc_lettings_site application."""

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_accueil_status_et_template(client):
    """Home page should return HTTP 200 and use index.html template."""
    reponse = client.get(reverse("index"))
    assert reponse.status_code == 200
    assert "index.html" in [template.name for template in reponse.templates]
    assert b"Profiles" in reponse.content
    assert b"Lettings" in reponse.content

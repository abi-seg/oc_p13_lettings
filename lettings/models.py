"""Models for lettings application."""

from django.db import models


class Address(models.Model):
    """Address model storing postal address information."""

    number = models.PositiveIntegerField(verbose_name="numéro")
    street = models.CharField(max_length=64, verbose_name="rue")
    city = models.CharField(max_length=64, verbose_name="ville")
    state = models.CharField(max_length=2, verbose_name="état")
    zip_code = models.PositiveIntegerField(verbose_name="code postal")
    country_iso_code = models.CharField(
        max_length=3, verbose_name="code pays ISO")

    class Meta:
        """Metadata options for the Address model."""

        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self) -> str:
        """Return a human-readable representation of the address."""
        representation_adresse = f"{self.number} {self.street}"
        return representation_adresse


class Letting(models.Model):
    """Letting model linking a title to an address."""

    title = models.CharField(max_length=256, verbose_name="titre")
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, verbose_name="adresse")

    def __str__(self) -> str:
        """Return the letting title as string representation."""
        return self.title

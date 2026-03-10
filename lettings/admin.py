
"""Admin configuration for lettings application."""

from django.contrib import admin
from .models import Address, Letting


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Admin interface for Address model."""
    list_display = ("number", "street", "city")


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    """Admin interface for Letting model."""
    list_display = ("title", "address")

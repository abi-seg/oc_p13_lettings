"""Admin configuration for profiles application."""

from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin interface for Profile model."""
    list_display = ("user", "favorite_city")

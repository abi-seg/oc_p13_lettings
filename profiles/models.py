"""Models for profiles application."""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Profile model extending the default User model."""
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="utilisateur",
        related_name="profil_nouveau",
        related_query_name="profil_nouveau",
        )
    favorite_city = models.CharField(
        max_length=64,
        blank=True,
        verbose_name="ville préférée",
    )

    def __str__(self) -> str:
        """Return the username as string representation."""
        return self.user.username
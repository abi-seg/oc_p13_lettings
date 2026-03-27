"""Views for the profiles application."""
from django.shortcuts import render
from .models import Profile
import logging
logger = logging.getLogger(__name__)


def index(request):
    """Displays the list of profiles."""
    logger.info("Affichage de la liste des profils")
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """Displays the details of a single profile."""
    logger.info("Affichage du profil pour l'utilisateur %s", username)
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)

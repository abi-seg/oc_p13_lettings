from django.shortcuts import render
from .models import Letting
import logging
logger=logging.getLogger(__name__)


def index(request):
    """Displays the list of lettings."""
    logger.info("Affichage de la liste des locations")
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)
    #raise Exception("Erreur de test 500")


def letting(request, letting_id):
    """Display the details of a single letting"""
    logger.info("Affichage du détail de la location %s",letting_id)
    letting = Letting.objects.get(id=letting_id)
    context = {"title": letting.title, "address": letting.address}
    return render(request, "lettings/letting.html", context)

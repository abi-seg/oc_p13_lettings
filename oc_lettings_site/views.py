from django.shortcuts import render
import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """Display the home page."""
    logger.info("Affichage de la page d'acceuil")
    return render(request, 'index.html')

def page_non_trouvee(request, exception):
    """ Render custom 404 error page. """
    logger.warning("Page non trouvée: %s",request.path)
    contexte = {
        "message": "La page demandée n'existe pas.",
    }
    return render(request, "404.html",contexte,status=404)

def erreur_serveur(request):
    """Render custom 500 error page. """
    logger.error("Erreur interne du serveur pour l'url %s",request.path)
    contexte = {
        "message": "Une erreur interne s'est produite.",
    }
    return render(request, "500.html", contexte, status=500)


def declencher_erreur(request):
    """Intentionally raise an exception to verify Sentry integration."""
    raise Exception("Erreur de test Sentry")
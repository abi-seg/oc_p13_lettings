from django.shortcuts import render


def index(request):
    """Display the home page."""
    return render(request, 'index.html')

def page_non_trouvee(request, exception):
    """ Render custom 404 error page. """
    contexte = {
        "message": "La page demandée n'existe pas.",
    }
    return render(request, "404.html",contexte,status=404)

def erreur_serveur(request):
    """Render custom 500 error page. """
    contexte = {
        "message": "Une erreur interne s'est produite.",
    }
    return render(request, "500.html", contexte, status=500)


# def declencher_erreur(request):
    """Intentionally raise an exception to test the 500 error page."""
    1 / 0  # Erreur volontaire (division par zéro)

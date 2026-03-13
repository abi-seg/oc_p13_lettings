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




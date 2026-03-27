"""URL configuration for the oc_lettings_site project. """
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include("lettings.urls", namespace="lettings")),
    path('profiles/', include("profiles.urls", namespace="profiles")),
    path('admin/', admin.site.urls),
    path("test-sentry/", views.declencher_erreur,
         name="test_sentry"),  # URL de test
]

handler404 = "oc_lettings_site.views.page_non_trouvee"
handler500 = "oc_lettings_site.views.erreur_serveur"

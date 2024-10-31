from django.urls import path
from .views import contactView, successView

urlpatterns = [
    path('contact/', contactView, name='contactView'),  # URL pour le formulaire de contact
    path('success/', successView, name='successView'),  # URL pour la page de succès
]

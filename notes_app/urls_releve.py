"""URLs – Relevé de notes (Rafael)"""

# On importe path pour définir les routes URL
from django.urls import path
# On importe nos vues
from . import views

urlpatterns = [
    # Page 1 : liste des étudiants pour choisir un relevé
    # Quand l'utilisateur va sur /releve/, Django appelle releve_liste
    path('', views.releve_liste, name='releve_liste'),

    # Page 2 : relevé détaillé d'un étudiant
    # <str:pk> capture le numéro étudiant dans l'URL (ex: /releve/6767/)
    # et le passe à la vue dans le paramètre 'pk'
    path('<str:pk>/', views.releve_etudiant, name='releve_etudiant'),
]
"""URLs – Étudiants"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.etudiant_liste, name='etudiant_liste'),
    path('ajouter/', views.etudiant_creer, name='etudiant_creer'),
    path('<str:pk>/', views.etudiant_detail, name='etudiant_detail'),
    path('<str:pk>/modifier/', views.etudiant_modifier, name='etudiant_modifier'),
    path('<str:pk>/supprimer/', views.etudiant_supprimer, name='etudiant_supprimer'),
]

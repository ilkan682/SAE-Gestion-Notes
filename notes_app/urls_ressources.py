from django.urls import path
from . import views

urlpatterns = [
    path('ressources/', views.ressource_liste, name='ressource_liste'),
    path('ressources/ajouter/', views.ressource_creer, name='ressource_create'),
    path('ressources/<int:pk>/', views.ressource_detail, name='ressource_detail'),
    path('ressources/<int:pk>/modifier/', views.ressource_modifier, name='ressource_update'),
    path('ressources/<int:pk>/supprimer/', views.ressource_supprimer, name='ressource_delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('ressources/', views.ressource_liste, name='ressource_liste'),
    path('ressources/ajouter/', views.ressource_creer, name='ressource_create'),
    path('ressources/<str:pk>/', views.ressource_detail, name='ressource_detail'),
    path('ressources/<str:pk>/modifier/', views.ressource_modifier, name='ressource_update'),
    path('ressources/<str:pk>/supprimer/', views.ressource_supprimer, name='ressource_delete'),
]
"""URLs – UE"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ue_liste, name='ue_liste'),
    path('ajouter/', views.ue_creer, name='ue_creer'),
    path('<str:pk>/', views.ue_detail, name='ue_detail'),
    path('<str:pk>/modifier/', views.ue_modifier, name='ue_modifier'),
    path('<str:pk>/supprimer/', views.ue_supprimer, name='ue_supprimer'),
]

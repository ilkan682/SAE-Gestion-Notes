
from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.releve_liste, name='releve_liste'),

    
    path('<str:pk>/', views.releve_etudiant, name='releve_etudiant'),
]
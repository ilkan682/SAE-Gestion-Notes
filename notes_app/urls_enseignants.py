
from django.urls import path
from . import views

urlpatterns = [
    path('', views.enseignant_liste, name='enseignant_liste'),
    path('ajouter/', views.enseignant_creer, name='enseignant_creer'),
    path('<int:pk>/modifier/', views.enseignant_modifier, name='enseignant_modifier'),
    path('<int:pk>/supprimer/', views.enseignant_supprimer, name='enseignant_supprimer'),
]

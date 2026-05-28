from django.urls import path
from . import views

urlpatterns = [
    path('examens/', views.examen_liste, name='examen_liste'),
    path('examens/ajouter/', views.examen_creer, name='examen_create'),
    path('examens/<int:pk>/', views.examen_detail, name='examen_detail'),
    path('examens/<int:pk>/modifier/', views.examen_modifier, name='examen_update'),
    path('examens/<int:pk>/supprimer/', views.examen_supprimer, name='examen_delete'),
]
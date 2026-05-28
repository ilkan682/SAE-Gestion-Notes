from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.note_liste, name='note_liste'),
    path('notes/ajouter/', views.note_creer, name='note_create'),
    path('notes/<int:pk>/modifier/', views.note_modifier, name='note_update'),
    path('notes/<int:pk>/supprimer/', views.note_supprimer, name='note_delete'),
]
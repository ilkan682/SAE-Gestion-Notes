"""
URLs principales du projet SAÉ Gestion des Notes
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from notes_app import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.accueil, name='accueil'),
    path('etudiants/', include('notes_app.urls_etudiants')),
    path('enseignants/', include('notes_app.urls_enseignants')),
    path('ue/', include('notes_app.urls_ue')),
    path('', include('notes_app.urls_ressources')),
    path('', include('notes_app.urls_examens')),
    path('', include('notes_app.urls_notes')),
    path('import/', include('notes_app.urls_import')),
    # Les URL des autres branches seront ajoutées ici lors de la fusion
    # path('ressources/', include('notes_app.urls_ressources')),   # dev-hussain
    # path('examens/', include('notes_app.urls_examens')),         # dev-hussain
    # path('notes/', include('notes_app.urls_notes')),             # dev-hussain + dev-rafael
    # path('import/', include('notes_app.urls_import')),           # dev-rafael
    # path('releve/', include('notes_app.urls_releve')),           # dev-rafael
    # path('import/', include('notes_app.urls_import')),   # dev-rafael
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class EtudiantForm(ModelForm):
    class Meta:
        model  = models.Etudiant
        fields = ('numero_etudiant', 'nom', 'prenom', 'groupe', 'email', 'photo')
        labels = {
            'numero_etudiant' : _('Numéro étudiant'),
            'nom'             : _('Nom'),
            'prenom'          : _('Prénom'),
            'groupe'          : _('Groupe'),
            'email'           : _('Adresse e-mail'),
            'photo'           : _('Photo'),
        }


class EnseignantForm(ModelForm):
    class Meta:
        model  = models.Enseignant
        fields = ('nom', 'prenom')
        labels = {
            'nom'    : _('Nom'),
            'prenom' : _('Prénom'),
        }


class UEForm(ModelForm):
    class Meta:
        model  = models.UE
        fields = ('code_ue', 'nom', 'semestre', 'credits_ects')
        labels = {
            'code_ue'      : _('Code UE'),
            'nom'          : _('Nom de l\'UE'),
            'semestre'     : _('Semestre'),
            'credits_ects' : _('Crédits ECTS'),
        }
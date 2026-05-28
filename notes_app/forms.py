"""
forms.py – Formulaires Django pour Étudiants, Enseignants et UE
Responsable : Personne 1 (Ilkan) – branche dev-ilkan
"""

from django import forms
from .models import Etudiant, Enseignant, UE, Ressource, Examen, Note


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['numero_etudiant', 'nom', 'prenom', 'groupe', 'email', 'photo']
        widgets = {
            'numero_etudiant': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 22015487'
            }),
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de famille'
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom'
            }),
            'groupe': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: BUT-INFO-1A'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'prenom.nom@etudiant.univ.fr'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'numero_etudiant': 'N° étudiant',
            'nom': 'Nom',
            'prenom': 'Prénom',
            'groupe': 'Groupe',
            'email': 'Adresse e-mail',
            'photo': 'Photo (optionnelle)',
        }


class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de famille'
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom'
            }),
        }


class UEForm(forms.ModelForm):
    class Meta:
        model = UE
        fields = ['code_ue', 'nom', 'semestre', 'credits_ects']
        widgets = {
            'code_ue': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: R1.01'
            }),
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Intitulé complet de l\'UE'
            }),
            'semestre': forms.Select(attrs={
                'class': 'form-select'
            }),
            'credits_ects': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 30
            }),
        }
        labels = {
            'code_ue': 'Code UE',
            'nom': 'Nom de l\'UE',
            'semestre': 'Semestre',
            'credits_ects': 'Crédits ECTS',
        }
class RessourceForm(forms.ModelForm):
    class Meta:
        model = Ressource
        fields = ['code_ressource', 'nom', 'descriptif', 'coefficient', 'ue']
        widgets = {
            'code_ressource': forms.TextInput(attrs={'class': 'form-control'}),
            'nom':            forms.TextInput(attrs={'class': 'form-control'}),
            'descriptif':     forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'coefficient':    forms.NumberInput(attrs={'class': 'form-control'}),
            'ue':             forms.Select(attrs={'class': 'form-select'}),
        }
class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['titre', 'date', 'coefficient']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            css = 'form-select' if hasattr(widget, 'choices') else 'form-control'
            widget.attrs['class'] = css


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['examen', 'etudiant', 'note', 'appreciation']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            css = 'form-select' if hasattr(widget, 'choices') else 'form-control'
            widget.attrs['class'] = css
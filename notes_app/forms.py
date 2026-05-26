"""
forms.py – Formulaires Django pour Étudiants, Enseignants et UE
Responsable : Personne 1 (Ilkan) – branche dev-ilkan
"""

from django import forms
from .models import Etudiant, Enseignant, UE


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

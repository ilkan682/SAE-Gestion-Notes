"""
views.py – Vues CRUD pour Étudiants, Enseignants et UE
Responsable : Personne 1 (Ilkan) – branche dev-ilkan
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Etudiant, Enseignant, UE
from .forms import EtudiantForm, EnseignantForm, UEForm


# ──────────────────────────────────────────────
#  PAGE D'ACCUEIL
# ──────────────────────────────────────────────

def accueil(request):
    """Tableau de bord principal avec statistiques."""
    context = {
        'nb_etudiants': Etudiant.objects.count(),
        'nb_enseignants': Enseignant.objects.count(),
        'nb_ue': UE.objects.count(),
        'titre_page': 'Tableau de bord',
    }
    return render(request, 'notes_app/accueil.html', context)


# ══════════════════════════════════════════════════════
#  CRUD – ÉTUDIANTS
# ══════════════════════════════════════════════════════

def etudiant_liste(request):
    """Affiche la liste de tous les étudiants avec recherche."""
    query = request.GET.get('q', '')
    etudiants = Etudiant.objects.all()

    if query:
        etudiants = etudiants.filter(
            Q(nom__icontains=query) |
            Q(prenom__icontains=query) |
            Q(numero_etudiant__icontains=query) |
            Q(groupe__icontains=query)
        )

    context = {
        'etudiants': etudiants,
        'query': query,
        'titre_page': 'Étudiants',
    }
    return render(request, 'notes_app/etudiant_liste.html', context)


def etudiant_detail(request, pk):
    """Affiche le détail d'un étudiant."""
    etudiant = get_object_or_404(Etudiant, pk=pk)
    context = {
        'etudiant': etudiant,
        'titre_page': f'{etudiant.prenom} {etudiant.nom}',
    }
    return render(request, 'notes_app/etudiant_detail.html', context)


def etudiant_creer(request):
    """Crée un nouvel étudiant."""
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            etudiant = form.save()
            messages.success(request, f'Étudiant {etudiant.prenom} {etudiant.nom} ajouté avec succès.')
            return redirect('etudiant_liste')
        else:
            messages.error(request, 'Erreur dans le formulaire. Veuillez corriger les champs indiqués.')
    else:
        form = EtudiantForm()

    return render(request, 'notes_app/etudiant_form.html', {
        'form': form,
        'titre_page': 'Ajouter un étudiant',
        'action': 'Ajouter',
    })


def etudiant_modifier(request, pk):
    """Modifie un étudiant existant."""
    etudiant = get_object_or_404(Etudiant, pk=pk)

    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()
            messages.success(request, f'Étudiant {etudiant.prenom} {etudiant.nom} modifié avec succès.')
            return redirect('etudiant_liste')
        else:
            messages.error(request, 'Erreur dans le formulaire. Veuillez corriger les champs indiqués.')
    else:
        form = EtudiantForm(instance=etudiant)

    return render(request, 'notes_app/etudiant_form.html', {
        'form': form,
        'etudiant': etudiant,
        'titre_page': f'Modifier {etudiant.prenom} {etudiant.nom}',
        'action': 'Modifier',
    })


def etudiant_supprimer(request, pk):
    """Supprime un étudiant après confirmation."""
    etudiant = get_object_or_404(Etudiant, pk=pk)

    if request.method == 'POST':
        nom_complet = f'{etudiant.prenom} {etudiant.nom}'
        etudiant.delete()
        messages.success(request, f'Étudiant {nom_complet} supprimé.')
        return redirect('etudiant_liste')

    return render(request, 'notes_app/confirmer_suppression.html', {
        'objet': etudiant,
        'type': 'l\'étudiant',
        'retour_url': 'etudiant_liste',
        'titre_page': 'Supprimer un étudiant',
    })


# ══════════════════════════════════════════════════════
#  CRUD – ENSEIGNANTS
# ══════════════════════════════════════════════════════

def enseignant_liste(request):
    """Affiche la liste des enseignants."""
    query = request.GET.get('q', '')
    enseignants = Enseignant.objects.all()

    if query:
        enseignants = enseignants.filter(
            Q(nom__icontains=query) | Q(prenom__icontains=query)
        )

    return render(request, 'notes_app/enseignant_liste.html', {
        'enseignants': enseignants,
        'query': query,
        'titre_page': 'Enseignants',
    })


def enseignant_creer(request):
    """Crée un nouvel enseignant."""
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            enseignant = form.save()
            messages.success(request, f'Enseignant {enseignant.prenom} {enseignant.nom} ajouté.')
            return redirect('enseignant_liste')
        else:
            messages.error(request, 'Erreur dans le formulaire.')
    else:
        form = EnseignantForm()

    return render(request, 'notes_app/enseignant_form.html', {
        'form': form,
        'titre_page': 'Ajouter un enseignant',
        'action': 'Ajouter',
    })


def enseignant_modifier(request, pk):
    """Modifie un enseignant existant."""
    enseignant = get_object_or_404(Enseignant, pk=pk)

    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            messages.success(request, f'Enseignant {enseignant.prenom} {enseignant.nom} modifié.')
            return redirect('enseignant_liste')
        else:
            messages.error(request, 'Erreur dans le formulaire.')
    else:
        form = EnseignantForm(instance=enseignant)

    return render(request, 'notes_app/enseignant_form.html', {
        'form': form,
        'enseignant': enseignant,
        'titre_page': f'Modifier {enseignant.prenom} {enseignant.nom}',
        'action': 'Modifier',
    })


def enseignant_supprimer(request, pk):
    """Supprime un enseignant."""
    enseignant = get_object_or_404(Enseignant, pk=pk)

    if request.method == 'POST':
        nom_complet = f'{enseignant.prenom} {enseignant.nom}'
        enseignant.delete()
        messages.success(request, f'Enseignant {nom_complet} supprimé.')
        return redirect('enseignant_liste')

    return render(request, 'notes_app/confirmer_suppression.html', {
        'objet': enseignant,
        'type': 'l\'enseignant',
        'retour_url': 'enseignant_liste',
        'titre_page': 'Supprimer un enseignant',
    })


# ══════════════════════════════════════════════════════
#  CRUD – UE
# ══════════════════════════════════════════════════════

def ue_liste(request):
    """Affiche la liste des UE."""
    query = request.GET.get('q', '')
    semestre = request.GET.get('semestre', '')
    ues = UE.objects.all()

    if query:
        ues = ues.filter(
            Q(code_ue__icontains=query) | Q(nom__icontains=query)
        )
    if semestre:
        ues = ues.filter(semestre=semestre)

    semestres = UE.SEMESTRES

    return render(request, 'notes_app/ue_liste.html', {
        'ues': ues,
        'query': query,
        'semestre_actif': semestre,
        'semestres': semestres,
        'titre_page': 'Unités d\'Enseignement',
    })


def ue_detail(request, pk):
    """Détail d'une UE avec ses ressources."""
    ue = get_object_or_404(UE, pk=pk)
    ressources = ue.ressources.all()
    return render(request, 'notes_app/ue_detail.html', {
        'ue': ue,
        'ressources': ressources,
        'titre_page': f'UE – {ue.code_ue}',
    })


def ue_creer(request):
    """Crée une nouvelle UE."""
    if request.method == 'POST':
        form = UEForm(request.POST)
        if form.is_valid():
            ue = form.save()
            messages.success(request, f'UE {ue.code_ue} – {ue.nom} ajoutée.')
            return redirect('ue_liste')
        else:
            messages.error(request, 'Erreur dans le formulaire.')
    else:
        form = UEForm()

    return render(request, 'notes_app/ue_form.html', {
        'form': form,
        'titre_page': 'Ajouter une UE',
        'action': 'Ajouter',
    })


def ue_modifier(request, pk):
    """Modifie une UE."""
    ue = get_object_or_404(UE, pk=pk)

    if request.method == 'POST':
        form = UEForm(request.POST, instance=ue)
        if form.is_valid():
            form.save()
            messages.success(request, f'UE {ue.code_ue} modifiée.')
            return redirect('ue_liste')
        else:
            messages.error(request, 'Erreur dans le formulaire.')
    else:
        form = UEForm(instance=ue)

    return render(request, 'notes_app/ue_form.html', {
        'form': form,
        'ue': ue,
        'titre_page': f'Modifier {ue.code_ue}',
        'action': 'Modifier',
    })


def ue_supprimer(request, pk):
    """Supprime une UE."""
    ue = get_object_or_404(UE, pk=pk)

    if request.method == 'POST':
        code = ue.code_ue
        ue.delete()
        messages.success(request, f'UE {code} supprimée.')
        return redirect('ue_liste')

    return render(request, 'notes_app/confirmer_suppression.html', {
        'objet': ue,
        'type': 'l\'UE',
        'retour_url': 'ue_liste',
        'titre_page': 'Supprimer une UE',
    })

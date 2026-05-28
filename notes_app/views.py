from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import EtudiantForm, EnseignantForm, UEForm
from . import models


# ══════════════════════════════════════════════
#  ACCUEIL
# ══════════════════════════════════════════════

def accueil(request):
    nb_etudiants  = models.Etudiant.objects.count()
    nb_enseignants = models.Enseignant.objects.count()
    nb_ue         = models.UE.objects.count()
    return render(request, "notes_app/accueil.html", {
        "nb_etudiants"  : nb_etudiants,
        "nb_enseignants": nb_enseignants,
        "nb_ue"         : nb_ue,
    })


# ══════════════════════════════════════════════
#  ÉTUDIANTS
# ══════════════════════════════════════════════

def etudiant_index(request):
    liste = list(models.Etudiant.objects.all())
    return render(request, "notes_app/etudiant_index.html", {"liste": liste})


def etudiant_ajout(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            etudiant = form.save()
            return render(request, "notes_app/etudiant_affiche.html", {"etudiant": etudiant})
        else:
            return render(request, "notes_app/etudiant_ajout.html", {"form": form})
    else:
        form = EtudiantForm()
        return render(request, "notes_app/etudiant_ajout.html", {"form": form})


def etudiant_read(request, id):
    etudiant = get_object_or_404(models.Etudiant, pk=id)
    return render(request, "notes_app/etudiant_affiche.html", {"etudiant": etudiant})


def etudiant_update(request, id):
    etudiant = get_object_or_404(models.Etudiant, pk=id)
    if request.method == "POST":
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('etudiant_index')
        else:
            return render(request, "notes_app/etudiant_update.html", {"form": form, "id": id})
    else:
        form = EtudiantForm(instance=etudiant)
        return render(request, "notes_app/etudiant_update.html", {"form": form, "id": id})


def etudiant_delete(request, id):
    etudiant = get_object_or_404(models.Etudiant, pk=id)
    etudiant.delete()
    return HttpResponseRedirect("/etudiants/")


# ══════════════════════════════════════════════
#  ENSEIGNANTS
# ══════════════════════════════════════════════

def enseignant_index(request):
    liste = list(models.Enseignant.objects.all())
    return render(request, "notes_app/enseignant_index.html", {"liste": liste})


def enseignant_ajout(request):
    if request.method == "POST":
        form = EnseignantForm(request.POST)
        if form.is_valid():
            enseignant = form.save()
            return render(request, "notes_app/enseignant_affiche.html", {"enseignant": enseignant})
        else:
            return render(request, "notes_app/enseignant_ajout.html", {"form": form})
    else:
        form = EnseignantForm()
        return render(request, "notes_app/enseignant_ajout.html", {"form": form})


def enseignant_read(request, id):
    enseignant = get_object_or_404(models.Enseignant, pk=id)
    return render(request, "notes_app/enseignant_affiche.html", {"enseignant": enseignant})


def enseignant_update(request, id):
    enseignant = get_object_or_404(models.Enseignant, pk=id)
    if request.method == "POST":
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('enseignant_index')
        else:
            return render(request, "notes_app/enseignant_update.html", {"form": form, "id": id})
    else:
        form = EnseignantForm(instance=enseignant)
        return render(request, "notes_app/enseignant_update.html", {"form": form, "id": id})


def enseignant_delete(request, id):
    enseignant = get_object_or_404(models.Enseignant, pk=id)
    enseignant.delete()
    return HttpResponseRedirect("/enseignants/")


# ══════════════════════════════════════════════
#  UE
# ══════════════════════════════════════════════

def ue_index(request):
    liste = list(models.UE.objects.all())
    return render(request, "notes_app/ue_index.html", {"liste": liste})


def ue_ajout(request):
    if request.method == "POST":
        form = UEForm(request.POST)
        if form.is_valid():
            ue = form.save()
            return render(request, "notes_app/ue_affiche.html", {"ue": ue})
        else:
            return render(request, "notes_app/ue_ajout.html", {"form": form})
    else:
        form = UEForm()
        return render(request, "notes_app/ue_ajout.html", {"form": form})


def ue_read(request, id):
    ue = get_object_or_404(models.UE, pk=id)
    return render(request, "notes_app/ue_affiche.html", {"ue": ue})


def ue_update(request, id):
    ue = get_object_or_404(models.UE, pk=id)
    if request.method == "POST":
        form = UEForm(request.POST, instance=ue)
        if form.is_valid():
            form.save()
            return redirect('ue_index')
        else:
            return render(request, "notes_app/ue_update.html", {"form": form, "id": id})
    else:
        form = UEForm(instance=ue)
        return render(request, "notes_app/ue_update.html", {"form": form, "id": id})


def ue_delete(request, id):
    ue = get_object_or_404(models.UE, pk=id)
    ue.delete()
    return HttpResponseRedirect("/ue/")
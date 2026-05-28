"""
models.py – SAÉ Gestion des Notes Étudiantes
Responsable : Personne 1 (Ilkan) – branche dev-ilkan

Ce fichier contient TOUS les modèles du projet afin que les migrations
soient cohérentes entre les branches. Les autres branches utiliseront
ces modèles dans leurs propres vues.
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# ══════════════════════════════════════════════════════
#  MODÈLES PERSONNE 1 – Étudiants, Enseignants, UE
# ══════════════════════════════════════════════════════

class Enseignant(models.Model):
    """Représente un enseignant."""
    id_enseignant = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")

    class Meta:
        db_table = 'enseignants'
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"
        ordering = ['nom', 'prenom']

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Etudiant(models.Model):
    """Représente un étudiant."""
    numero_etudiant = models.CharField(
        max_length=20,
        primary_key=True,
        verbose_name="N° étudiant"
    )
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    groupe = models.CharField(max_length=20, verbose_name="Groupe")
    email = models.EmailField(unique=True, verbose_name="Email")
    photo = models.ImageField(
        upload_to='photos_etudiants/',
        blank=True,
        null=True,
        verbose_name="Photo"
    )

    # Relation Many-to-Many explicite via la table intermédiaire Note
    examens = models.ManyToManyField(
        'Examen',
        through='Note',
        related_name='etudiants',
        verbose_name="Examens"
    )

    class Meta:
        db_table = 'etudiants'
        verbose_name = "Étudiant"
        verbose_name_plural = "Étudiants"
        ordering = ['nom', 'prenom']

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.numero_etudiant})"

    def get_initiales(self):
        return f"{self.prenom[0]}{self.nom[0]}".upper()


class UE(models.Model):
    """Unité d'Enseignement (ex: UE1.2, UE1.3)."""
    SEMESTRES = [
        ('S1', 'Semestre 1'),
        ('S2', 'Semestre 2'),
        ('S3', 'Semestre 3'),
        ('S4', 'Semestre 4'),
        ('S5', 'Semestre 5'),
        ('S6', 'Semestre 6'),
    ]

    code_ue = models.CharField(
        max_length=20,
        primary_key=True,
        verbose_name="Code UE"
    )
    nom = models.CharField(max_length=200, verbose_name="Nom de l'UE")
    semestre = models.CharField(
        max_length=2,
        choices=SEMESTRES,
        verbose_name="Semestre"
    )
    credits_ects = models.PositiveSmallIntegerField(
        verbose_name="Crédits ECTS",
        validators=[MinValueValidator(1), MaxValueValidator(30)]
    )

    class Meta:
        db_table = 'ue'
        verbose_name = "UE"
        verbose_name_plural = "UE"
        ordering = ['semestre', 'code_ue']

    def __str__(self):
        return f"{self.code_ue} – {self.nom}"


# ══════════════════════════════════════════════════════
#  MODÈLES PERSONNE 2 – Ressources, Examens, Notes
# ══════════════════════════════════════════════════════

class Ressource(models.Model):
    """Ressource pédagogique (Matière) associée à une UE."""
    code_ressource = models.CharField(
        max_length=20,
        primary_key=True,
        verbose_name="Code ressource"
    )
    nom = models.CharField(max_length=200, verbose_name="Nom")
    descriptif = models.TextField(blank=True, verbose_name="Descriptif")
    coefficient = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=1.0,
        verbose_name="Coefficient"
    )
    ue = models.ForeignKey(
        UE,
        on_delete=models.CASCADE,
        related_name='ressources',
        verbose_name="UE associée"
    )

    # Association d'un enseignant responsable à la ressource
    enseignant_responsable = models.ForeignKey(
        Enseignant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ressources_gerees',
        verbose_name="Enseignant responsable"
    )

    class Meta:
        db_table = 'ressources'
        verbose_name = "Ressource"
        verbose_name_plural = "Ressources"
        ordering = ['ue', 'code_ressource']

    def __str__(self):
        return f"{self.code_ressource} – {self.nom}"


class Examen(models.Model):
    """Examen lié à une ressource (ex: DS, TP, SAE)."""
    id_examen = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200, verbose_name="Titre")
    date = models.DateField(verbose_name="Date")
    coefficient = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=1.0,
        verbose_name="Coefficient"
    )
    ressource = models.ForeignKey(
        Ressource,
        on_delete=models.CASCADE,
        related_name='examens',
        verbose_name="Ressource associée"
    )

    class Meta:
        db_table = 'examens'
        verbose_name = "Examen"
        verbose_name_plural = "Examens"
        ordering = ['-date', 'titre']

    def __str__(self):
        return f"{self.titre} ({self.ressource.code_ressource})"


class Note(models.Model):
    """Table intermédiaire associant un Étudiant à un Examen avec sa Note."""
    id_note = models.AutoField(primary_key=True)
    etudiant = models.ForeignKey(
        Etudiant,
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name="Étudiant"
    )
    examen = models.ForeignKey(
        Examen,
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name="Examen"
    )
    note = models.FloatField(
        verbose_name="Note",
        validators=[MinValueValidator(0.0), MaxValueValidator(20.0)]
    )

    class Meta:
        db_table = 'notes'
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        unique_together = [('etudiant', 'examen')]  # Un étudiant n'a qu'une seule note par examen

    def __str__(self):
        return f"{self.etudiant.prenom} {self.etudiant.nom} – {self.examen.titre} : {self.note}/20"
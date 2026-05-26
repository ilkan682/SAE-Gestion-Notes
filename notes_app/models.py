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

    class Meta:
        db_table = 'etudiants'
        verbose_name = "Étudiant"
        verbose_name_plural = "Étudiants"
        ordering = ['nom', 'prenom']

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.numero_etudiant})"

    def get_initiales(self):
        return f"{self.prenom[0]}{self.nom[0]}".upper()


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


class UE(models.Model):
    """Unité d'Enseignement."""
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
#  (définis ici pour que les migrations fonctionnent)
# ══════════════════════════════════════════════════════

class Ressource(models.Model):
    """Ressource pédagogique associée à une UE."""
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

    class Meta:
        db_table = 'ressources'
        verbose_name = "Ressource"
        verbose_name_plural = "Ressources"
        ordering = ['ue', 'code_ressource']

    def __str__(self):
        return f"{self.code_ressource} – {self.nom}"


class Examen(models.Model):
    """Examen lié à une ressource."""
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
        ordering = ['-date']

    def __str__(self):
        return f"{self.titre} ({self.date})"


class Note(models.Model):
    """Note d'un étudiant à un examen."""
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
    note = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(20)],
        verbose_name="Note /20"
    )
    appreciation = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Appréciation"
    )

    class Meta:
        db_table = 'notes'
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        # Contrainte d'unicité : un étudiant ne peut avoir qu'une note par examen
        unique_together = [('etudiant', 'examen')]

    def __str__(self):
        return f"{self.etudiant} – {self.examen} : {self.note}/20"

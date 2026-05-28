from django.db import models

# ──────────────────────────────────────────────
#  MODÈLES – branche dev-ilkan (Personne 1)
#  Les modèles Ressource, Examen, Note sont aussi
#  définis ici pour que les migrations soient
#  cohérentes entre les 3 branches.
# ──────────────────────────────────────────────

class Etudiant(models.Model):
    numero_etudiant = models.CharField(max_length=20, primary_key=True)
    nom             = models.CharField(max_length=100)
    prenom          = models.CharField(max_length=100)
    groupe          = models.CharField(max_length=20)
    email           = models.EmailField(unique=True)
    photo           = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.numero_etudiant})"


class Enseignant(models.Model):
    nom    = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class UE(models.Model):
    SEMESTRES = [
        ('S1', 'Semestre 1'), ('S2', 'Semestre 2'),
        ('S3', 'Semestre 3'), ('S4', 'Semestre 4'),
        ('S5', 'Semestre 5'), ('S6', 'Semestre 6'),
    ]
    code_ue      = models.CharField(max_length=20, primary_key=True)
    nom          = models.CharField(max_length=200)
    semestre     = models.CharField(max_length=2, choices=SEMESTRES)
    credits_ects = models.IntegerField()

    def __str__(self):
        return f"{self.code_ue} – {self.nom}"


# ── Modèles pour les autres branches (dev-hussain, dev-rafael) ──

class Ressource(models.Model):
    code_ressource = models.CharField(max_length=20, primary_key=True)
    nom            = models.CharField(max_length=200)
    descriptif     = models.TextField(blank=True, null=True)
    coefficient    = models.FloatField(default=1.0)
    ue             = models.ForeignKey(UE, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code_ressource} – {self.nom}"


class Examen(models.Model):
    titre      = models.CharField(max_length=200)
    date       = models.DateField()
    coefficient = models.FloatField(default=1.0)
    ressource  = models.ForeignKey(Ressource, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titre} ({self.date})"


class Note(models.Model):
    etudiant    = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    examen      = models.ForeignKey(Examen, on_delete=models.CASCADE)
    note        = models.FloatField()
    appreciation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = [('etudiant', 'examen')]

    def __str__(self):
        return f"{self.etudiant} – {self.examen} : {self.note}/20"
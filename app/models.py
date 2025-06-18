from django.db import models

class Personnes(models.Model):
    AMATEUR = 'AMATEUR'
    PROFESSIONNEL = 'PROFESSIONNEL'

    CHOIX_TYPE = [
        (AMATEUR, 'Amateur'),
        (PROFESSIONNEL, 'Professionnel'),
    ]

    pseudo = models.CharField(max_length=75, blank=False)
    nom = models.CharField(max_length=75, blank=False)
    prenom = models.CharField(max_length=75, blank=False)
    mail = models.EmailField(max_length=75, blank=False)
    motdepasse = models.CharField(max_length=75, blank=False)
    type = models.CharField(
        max_length=13,
        choices=CHOIX_TYPE,
        default=AMATEUR,
    )

    def __str__(self):
        chaine = f"{self.pseudo}"
        return chaine

    def dico(self):
        return {"pseudo": self.pseudo,
                "nom": self.nom,
                "prenom": self.nom,
                "mail": self.mail,
                "motdepasse": self.motdepasse,
                "type": self.type
                }


class Acteur(models.Model):
    nom = models.CharField(max_length=75, blank=False)
    prenom = models.CharField(max_length=75, blank=False)
    age = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        chaine = f"{self.prenom} {self.nom}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "prenom": self.prenom, "age": self.age, "photo": self.photo}


class Commentaire(models.Model):
    film = models.ForeignKey("film", on_delete=models.CASCADE, default=None, blank=False)
    personne = models.ForeignKey("personnes", on_delete=models.CASCADE, default=None, blank=False)
    note = models.IntegerField(blank=False)
    commentaire = models.TextField(null=True, blank=False)
    date = models.DateField(blank=False)

    def __str__(self):
        chaine = f"Note : {self.note}, De {self.personne}, pour le film : {self.film}"
        return chaine

    def dico(self):
        return {"film": self.film,
                "personne": self.personne,
                "note": self.note,
                "commentaire": self.commentaire,
                "date": self.date
                }

class Film(models.Model):
    titre = models.CharField(max_length=75, blank=False)
    categorie = models.ForeignKey("categorie", on_delete=models.CASCADE, default=None, blank=False)
    annee = models.DateField(blank=False)
    realisateur = models.CharField(max_length=75, blank=False)
    affiche = models.ImageField(upload_to='photos/', blank=True, null=True)
    acteur = models.ManyToManyField(Acteur, related_name='film')

    def __str__(self):
        chaine = f"{self.titre}"
        return chaine

    def dico(self):
        return {"titre": self.titre,"categorie": self.categorie, "annee": self.annee, "realisateur": self.realisateur,
                "affiche": self.affiche, "acteur": self.acteur}


class Categorie(models.Model):
    nom = models.CharField(max_length=75, blank=False)
    description = models.TextField(blank=False)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "description": self.description}

class Casting(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    acteur = models.ForeignKey(Acteur, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.film} {self.acteur}"

    def dicoUtilisateur(self):
        return f"{self.film}"

class CategorieFilm(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    descriptif = models.TextField(max_length=255)  # ← max_length sur TextField n’est pas utilisé par Django

    def __str__(self):
        return self.nom


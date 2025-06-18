from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from . import models
from .forms import CategorieForm, FilmForm
from .models import Film, Categorie


def index(request):
    liste = list(models.Categorie.objects.all())
    return render(request, "categories/index-categories.html", {"liste": liste})


def ajout(request):
    if request.method == "POST":
        form = CategorieForm(request)
        return render(request, "categories/ajout-categories.html", {"form" : form})
    else :
        form = CategorieForm
        return render(request, "categories/ajout-categories.html", {"form" : form})


def traitement(request):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        categorie = cform.save()
        return HttpResponseRedirect("/app/index-categories/")
    else:
        return render(request, "categories/ajout-categories.html", {"form": cform})


def affiche(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    return render(request, "categories/affiche-categories.html", {"categorie": categorie})


def update(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    if request.method == "POST":
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/index-categories/")
    else:
        form = CategorieForm(instance=categorie)
    return render(request, "categories/ajout-categories.html", {"form": form, "id": id})


def updatetraitement(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    if request.method == "POST":
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/index-categories/")
    else:
        form = CategorieForm(instance=categorie)
    return render(request, "categories/ajout-categories.html", {"form": form, "id": id})


def delete(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/app/index-categories/")

def films_par_categorie(request, id):
    categorie = get_object_or_404(Categorie, pk=id)
    films = Film.objects.filter(categorie=categorie)


    return render(request, 'categories/films_par_categorie.html', {
        'categorie': categorie,
        'films': films,
        'titre': f"Films dans la catégorie : {categorie.nom}"
    })
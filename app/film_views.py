from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import FilmForm
from . import models
from .models import Film, Acteur, Categorie, Commentaire
import csv

def index(request):
    liste = list(models.Film.objects.all())
    return render(request, "films/index-films.html", {"liste": liste})

def ajout(request):
    if request.method == "POST":
        form = FilmForm(request)
        return render(request, "films/ajout-films.html", {"form" : form})
    else :
        form = FilmForm
        return render(request, "films/ajout-films.html", {"form" : form})

def traitement(request):
    fform = FilmForm(request.POST, request.FILES)
    if fform.is_valid():
        film = fform.save()
        return HttpResponseRedirect("/app/index-films/")
    else:
        return render(request, "films/ajout-films.html", {"form": fform})

def affiche(request, id):
    film = models.Film.objects.get(pk=id)
    return render(request, "films/affiche-films.html", {"film": film})

def update(request, id):
    film = models.Film.objects.get(pk=id)
    if request.method == "POST":
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/index-films/")
    else:
        form = FilmForm(instance=film)
    return render(request, "films/ajout-films.html", {"form": form, "id": id})

def updatetraitement(request, id):
    film = models.Film.objects.get(pk=id)
    if request.method == "POST":
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/index-films/")
    else:
        form = FilmForm(instance=film)
    return render(request, "films/ajout-films.html", {"form": form, "id": id})

def delete(request, id):
    film = models.Film.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/app/index-films/")

from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import ActeurForm
from . import models


def index(request):
    liste = list(models.Acteur.objects.all())
    return render(request, "acteurs/index-acteurs.html", {"liste": liste})


def ajout(request):
    if request.method == "POST":
        form = ActeurForm(request)
        return render(request, "acteurs/ajout-acteurs.html", {"form" : form})
    else :
        form = ActeurForm
        return render(request, "acteurs/ajout-acteurs.html", {"form" : form})


def traitement(request):
    aform = ActeurForm(request.POST, request.FILES)
    if aform.is_valid():
        acteur = aform.save()
        return HttpResponseRedirect("/app/index-acteurs/")
    else:
        return render(request, "acteurs/ajout-acteurs.html", {"form": aform})


def affiche(request, id):
    acteur = models.Acteur.objects.get(pk=id)
    return render(request, "acteurs/affiche-acteurs.html", {"acteur": acteur})


def update(request, id):
    acteur = models.Acteur.objects.get(pk=id)
    if request.method == "POST":
        form = ActeurForm(request.POST, instance=acteur)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/index-acteurs/")
    else:
        form = ActeurForm(instance=acteur)
    return render(request, "acteurs/ajout-acteurs.html", {"form": form, "id": id})


def updatetraitement(request, id):
    acteur = models.Acteur.objects.get(pk=id)
    if request.method == "POST":
        form = ActeurForm(request.POST, instance=acteur)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/index-acteurs/")
    else:
        form = ActeurForm(instance=acteur)
    return render(request, "acteurs/ajout-acteurs.html", {"form": form, "id": id})


def delete(request, id):
    acteur = models.Acteur.objects.get(pk=id)
    acteur.delete()
    return HttpResponseRedirect("/app/index-acteurs/")
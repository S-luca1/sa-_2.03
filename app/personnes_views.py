from django.shortcuts import render, HttpResponseRedirect
from .forms import PersonnesForm
from . import models

def index(request):
    liste = list(models.Personnes.objects.all())
    return render(request, "personnes/index-personnes.html", {"liste": liste})


def ajout(request):
    if request.method == "POST":
        form = PersonnesForm(request)
        return render(request, "personnes/ajout-personnes.html", {"form" : form})
    else :
        form = PersonnesForm
        return render(request, "personnes/ajout-personnes.html", {"form" : form})


def traitement(request):
    tform = PersonnesForm(request.POST)
    if tform.is_valid():
        personne = tform.save()
        return HttpResponseRedirect("/app/index-personnes/")
    else:
        return render(request, "personnes/ajout-personnes.html", {"form": uform})


def affiche(request, id):
    personne = models.Personnes.objects.get(pk=id)
    return render(request, "personnes/affiche-personnes.html", {"personne": personne})


def update(request, id):
    personne = models.Personnes.objects.get(pk=id)
    if request.method == "POST":
        form = PersonnesForm(request.POST, instance=personne)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/index-personnes/")
    else:
        form = PersonnesForm(instance=personne)
    return render(request, "personnes/ajout-personnes.html", {"form": form, "id": id})


def updatetraitement(request, id):
    personne = models.Personnes.objects.get(pk=id)
    if request.method == "POST":
        form = PersonnesForm(request.POST, instance=personne)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/index-personnes/")
    else:
        form = PersonnesForm(instance=personne)
    return render(request, "personnes/ajout-personnes.html", {"form": form, "id": id})


def delete(request, id):
    personne = models.Personnes.objects.get(pk=id)
    personne.delete()
    return HttpResponseRedirect("/app/index-personnes/")
from django.urls import path
from . import personnes_views, commentaires_views, film_views, categories_views, acteurs_views

urlpatterns = [

# pages pour les personnes
    path("index-personnes/", personnes_views.index),
    path("traitement-personnes/", personnes_views.traitement),
    path("ajout-personnes/", personnes_views.ajout),
    path("affiche-personnes/<int:id>/", personnes_views.affiche),
    path("update-personnes/<int:id>/", personnes_views.update),
    path("updatetraitement-personnes/<int:id>/", personnes_views.updatetraitement),
    path("delete-personnes/<int:id>/", personnes_views.delete),

#pages pour les commentaires
    path("index-commentaires/", commentaires_views.index),
    path("traitement-commentaires/", commentaires_views.traitement),
    path("ajout-commentaires/", commentaires_views.ajout),
    path("affiche-commentaires/<int:id>/", commentaires_views.affiche),
    path("update-commentaires/<int:id>/", commentaires_views.update),
    path("updatetraitement-commentaires/<int:id>/", commentaires_views.updatetraitement),
    path("delete-commentaires/<int:id>/", commentaires_views.delete),
    path("commentaire_par_film/<int:film_id>/", commentaires_views.commentaires_par_film, name='commentaires-par-film'),

#pages pour les films
    path("index-films/", film_views.index),
    path("traitement-films/", film_views.traitement),
    path("ajout-films/", film_views.ajout),
    path("affiche-films/<int:id>/", film_views.affiche),
    path("update-films/<int:id>/", film_views.update),
    path("updatetraitement-films/<int:id>/", film_views.updatetraitement),
    path("delete-films/<int:id>/", film_views.delete),

#pages pour les catégories
    path("index-categories/", categories_views.index),
    path("traitement-categories/", categories_views.traitement),
    path("ajout-categories/", categories_views.ajout),
    path("affiche-categories/<int:id>/", categories_views.affiche),
    path("update-categories/<int:id>/", categories_views.update),
    path("updatetraitement-categories/<int:id>/", categories_views.updatetraitement),
    path("delete-categories/<int:id>/", categories_views.delete),
    path("films_par_categories/<int:id>/", categories_views.films_par_categorie),

#pages pour les acteurs
    path("index-acteurs/", acteurs_views.index),
    path("traitement-acteurs/", acteurs_views.traitement),
    path("ajout-acteurs/", acteurs_views.ajout),
    path("affiche-acteurs/<int:id>/", acteurs_views.affiche),
    path("update-acteurs/<int:id>/", acteurs_views.update),
    path("updatetraitement-acteurs/<int:id>/", acteurs_views.updatetraitement),
    path("delete-acteurs/<int:id>/", acteurs_views.delete),
    ]

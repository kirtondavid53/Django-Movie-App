from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movie_details/<str:pk>", views.movie_details, name="movie_details"),
    path("search", views.search, name="search")
]
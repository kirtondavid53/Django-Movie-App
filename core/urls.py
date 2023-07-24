from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movie_details/<str:pk>", views.movie_details, name="movie_details"),
    path("search", views.search, name="search"),
    path("add_favourite", views.add_favourite, name="add_favourite"),
    path("search", views.search, name="search"),
    path("favourites", views.view_favourites, name="favourites"),
    path("get_favor", views.get_favourites, name="get_favor"),
    path("del_favourite/<str:movie_id>", views.del_favourite, name="del_favourite"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", views.logout_view, name="logout"),
]
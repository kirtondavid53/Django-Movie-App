from django.shortcuts import render
from django.conf import settings

def index(request):
    name = 'David'
    return render(request, 'index.html', {'name':name, 'ACCESS_TOKEN':settings.ACCESS_TOKEN})

def movie_details(request, pk):
    return render(request, 'movie_details.html', {'movie_id':pk, 'ACCESS_TOKEN':settings.ACCESS_TOKEN})

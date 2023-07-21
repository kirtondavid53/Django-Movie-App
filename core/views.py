from django.shortcuts import render
from django.conf import settings

def index(request):
    return render(request, 'index.html', {'ACCESS_TOKEN':settings.ACCESS_TOKEN})

def movie_details(request, pk):
    return render(request, 'movie_details.html', {'movie_id':pk, 'ACCESS_TOKEN':settings.ACCESS_TOKEN})

def search(request):
    search = request.POST['search']
    return render(request, 'search.html', {'ACCESS_TOKEN':settings.ACCESS_TOKEN, 'search':search})

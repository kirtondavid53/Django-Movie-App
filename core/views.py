from django.shortcuts import render
from django.conf import settings

def index(request):
    name = 'David'
    return render(request, 'index.html', {'name':name, 'ACCESS_TOKEN':settings.ACCESS_TOKEN})
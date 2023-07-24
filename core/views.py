from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Favourite
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import json

def index(request):
    return render(request, 'index.html', {'ACCESS_TOKEN':settings.ACCESS_TOKEN})

def movie_details(request, pk):
    return render(request, 'movie_details.html', {'movie_id':pk, 'ACCESS_TOKEN':settings.ACCESS_TOKEN})

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        return render(request, 'search.html', {'ACCESS_TOKEN':settings.ACCESS_TOKEN, 'search':search})
    else:
        return redirect('index')

  
@csrf_exempt    
def add_favourite(request): #Also deletes if favourite already exit
    data = json.loads(request.body)
    movie_id = data['movie_id']
    movie_name = data['movie_name']
    user = request.user
    print(user)
    favourite = Favourite.objects.filter(user=user, movie_id=movie_id).first()
    if favourite is None:
        favourite = Favourite.objects.create(user=user,movie_id=movie_id)
        favourite.save()
        return JsonResponse({"message" : f'{movie_name} was added to your favourites', "isExit" : True}, safe=False)
    else:
        favourite.delete()
        return JsonResponse({"message" : f'{movie_name} was removed from your favourites', "isExit" : False}, safe=False)
    

@login_required(login_url="login")    
def view_favourites(request):
    return render(request, 'favor.html', {'ACCESS_TOKEN':settings.ACCESS_TOKEN})

@login_required(login_url="index") 
def get_favourites(request):
    user = request.user
    favourites = Favourite.objects.filter(user=user)

    return JsonResponse({"result" : list(favourites.values())})


@login_required(login_url="login")
def del_favourite(request, movie_id):
    user = request.user
    fav = Favourite.objects.get(user=user, movie_id=movie_id)
    fav.delete()
    messages.info(request, "Movie was removed from your favourites")
    return redirect("favourites")

def login_view(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            
            login(request, user)
            messages.info(request, "You have successfully logged in")
            return redirect('/')

        else:
            messages.info(request, "Invalid Credentials")  
            return redirect('login')

    else:  
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email is already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.warning(request, 'Username has already been used')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                user.save()
                login(request, user)
                messages.info(request, "Your account has been successfully created")
                return redirect('index')
            
        else:
            messages.warning(request, 'Passwords are not the name')
            return redirect(request, 'register')
        
    else:

        return render(request ,'register.html')
    

def logout_view(request):
    logout(request)
    messages.info(request, "You logged out")
    return redirect("index")
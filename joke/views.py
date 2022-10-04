import imp
from urllib import request
from django.shortcuts import render, redirect
# biblioteca de Django para una interfas de crear y autenticar usuarios
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# biblioteca de Django para crear usuarios
from django.contrib.auth.models import User
#para que el navegador pueda autenticar el usuario atravez de las cookes
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

from joke.models import usuario

# Create your views here.


def home(request):

    return render(request, 'home.html', {
        'form': UserCreationForm
    })


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            # Aqui se crean los usuarios
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(joke)
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": "Usuario ya existe"
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": "Contraseña incorrecta"
        })



def joke(request):

    return render(request, 'joke.html')

def signout(request):
    logout(request) 
    return (redirect('home'))

def signin(request):
    #envian formularios
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    #envian datos
    else:
        #datos validos
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        #en caso de que el usuario NO exista
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Ususario o contraseña es incorrecto'
            })
        else:
        #SI existe envialo a la pagina joke
            login(request, user)
            return redirect('joke')

        
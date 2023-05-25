from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,get_user_model
from .models import CustomUser,UserFav

import authentication
# Create your views here.

def home(request):
    return render(request,"index.html")


def signup(request):

    if request.method =="POST":
        usuario =  request.POST.get('Usuario')
        email = request.POST.get('email')
        senha1 = request.POST.get('senha')
        senha2 = request.POST.get('senha2')
        
        if senha1 != senha2:
            messages.error(request, 'As senhas não correspondem.')
            return redirect('home')

        user = get_user_model()
        user = user.objects.create_user(email=email,password=senha1,username=usuario)
        user.save()

        messages.success(request, "Sua conta foi criada com sucesso!")

        return redirect('signin')



    return render(request,"signup.html")

def signin(request):

    if request.method == "POST":
        usuario = request.POST.get('Usuario')
        senha = request.POST.get('senha')

        user = authenticate(request, username= usuario, password=senha)

        if usuario is not  None:
            login(request, user)
            return render(request,"index.html",{'usuario':user})

        else:
            messages.error(request,"Usuário não encontrado")

            return redirect('home')


    return render(request,"signin.html")

def signout(request):
    LOGOUT(request)
    messages.success(request,"Deslogado com sucesso")

    return redirect('home')

def fav(request):
    latest_manga_list = UserFav.objects.filter(usuario_id=2)
    usuario = get_user_model().objects.get(ID=2).get_username
    context = {
        'latest_manga_list' : latest_manga_list,
        'usuario' : usuario
    }
    return render(request, "fav.html", context)

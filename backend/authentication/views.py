from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

import authentication
# Create your views here.

def home(request):
    return render(request,"index.html")


def signup(request):

    if request.method =="Post":
        usuario =  request.Post['usuario']
        email = request.Post['email']
        senha1 = request.Post['senha']
        senha2 = request.Post['csenha']
        
        myuser = User.objects.create_user(usuario,email,senha1,senha2)
        myuser.save()

        messages.success(request, "Sua conta foi criada com sucesso!")

        return redirect('signin')



    return render(request,"signup.html")

def signin(request):

    if request.method == "POST":
        usuario = request.Post['usuario']
        senha = request.Post['senha']

        usuario = authentication(usuario = usuario,senha = senha)

        if usuario is not  None:
            login(request, usuario)
            usuario = usuario
            return render(request,"index.html",{'usuario':usuario})

        else:
            messages.error(request,"Usuário não encontrado")

            return redirect('home')


    return render(request,"signin.html")

def signout(request):
    LOGOUT(request)
    messages.success(request,"Deslogado com sucesso")

    return redirect('home')
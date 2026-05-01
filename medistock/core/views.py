from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Producto

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user:
            login(request, user)

            if user.rol =="cliente":
                return redirect("cliente")
            elif user.rol == "ejecutivo":
                return redirect("ejecutivo")
            elif user.rol == "logistica":
                return redirect("logistica")
            elif user.rol == "finanzas":
                return redirect("finanzas")
            
    return render(request, "core/login.html")


def cliente_view(request):
    productos = Producto.objects.all()
    return render(request, "cliente.html", {"productos": productos})

def ejecutivo_view(request):
    productos = Producto.objects.all()
    return render(request, "ejecutivo.html", {"productos": productos})

def logistica_view(request):
    productos = Producto.objects.all()
    return render(request, "logistica.html", {"productos": productos})

def finanzas_view(request):
    productos = Producto.objects.all()
    return render(request, "finanzas.html", {"productos": productos})
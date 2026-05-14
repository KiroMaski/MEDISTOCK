from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Producto, Pedido

def login_view(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        print(username)
        print(password)

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print(user)

        if user is not None:
            login(request, user)

            if user.rol == "cliente":
                return redirect("cliente")
            elif user.rol == "ejecutivo":
                return redirect("ejecutivo")
            elif user.rol == "logistica":
                return redirect("logistica")
            elif user.rol == "finanzas":
                return redirect("finanzas")
            
    return render(request, "login.html")


def cliente_view(request):
    productos = Producto.objects.all()
    return render(request, "cliente.html", {"productos": productos})

def ejecutivo_view(request):
    productos = Producto.objects.all()
    pedidos = Pedido.objects.all()
    return render(request, "ejecutivo.html", {"productos": productos, "pedidos": pedidos})

def logistica_view(request):
    productos = Producto.objects.all()
    pedidos = Pedido.objects.all()
    return render(request, "logistica.html", {"productos": productos, "pedidos": pedidos})

def finanzas_view(request):
    productos = Producto.objects.all()
    pedidos = Pedido.objects.all()
    return render(request, "finanzas.html", {"productos": productos, "pedidos": pedidos})

def tracking_view(request):
    return render(request, "tracking.html")
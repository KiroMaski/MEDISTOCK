from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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

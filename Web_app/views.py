from django.shortcuts import render, HttpResponse 

# Create your views here.

def Inicio(request):
    return render(request,"Web_app/Inicio.html")

def Tienda(request):
    return render(request,"Web_app/Tienda.html")
     

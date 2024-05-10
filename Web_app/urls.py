from django.urls import path

from Web_app import views

urlpatterns = [
    path('',views.Inicio,name="Inicio"),
    path('Tienda',views.Tienda,name="Tienda"),
]

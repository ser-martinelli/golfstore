
from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('productos/', views.lista_productos, name="productos"),
    path('crear-producto/', views.crear_producto, name="crear_producto"),
    path('buscar-producto/', views.buscar_producto, name="buscar_producto"),
    path('about/', views.about, name="about"),
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_request, name="logout"),

]
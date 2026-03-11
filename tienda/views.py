
from django.shortcuts import render, redirect
from .models import Categoria
from .models import Producto
from .forms import ProductoFormulario, BuscarProducto

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def inicio(request):
    return render(request, "home/inicio.html")

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/lista.html", {"productos": productos})

def crear_producto(request):
    if request.method == "POST":
        formulario = ProductoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("productos")
    else:
        formulario = ProductoFormulario()
    return render(request, "productos/crear.html", {"form": formulario})

def buscar_producto(request):
    productos = None
    if request.GET.get("nombre"):
        nombre = request.GET["nombre"]
        productos = Producto.objects.filter(nombre__icontains=nombre)
    return render(request, "productos/buscar.html", {"productos": productos})

def about(request):
    return render(request, "about.html")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=password)
            if user:
                login(request, user)
                return redirect("inicio")
    else:
        form = AuthenticationForm()
    return render(request, "usuarios/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "usuarios/register.html", {"form": form})

def logout_request(request):
    logout(request)
    return redirect("inicio")

def detalle_producto(request, id):
    producto = Producto.objects.get(id=id)
    return render(request,
    "productos/detalle.html",
    {"producto": producto})

def categorias(request):

    categorias = Categoria.objects.all()

    return render(request,
    "categorias/lista.html",
    {"categorias": categorias})
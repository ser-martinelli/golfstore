
from django import forms
from .models import Producto

class ProductoFormulario(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'


class BuscarProducto(forms.Form):

    nombre = forms.CharField(max_length=100)
from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        field = '__all__'

from django import forms

from .models import Produto, Venda


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = "__all__"


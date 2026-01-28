from django.shortcuts import render
from django.http import HttpResponse

from .models import Cliente, Produto, Venda
from .forms import ProdutoForm, VendaForm

# Create your views here.
def index_view(request):
    return render(request, "index.html")

def sobre_view(request):
    return render(request, "sobre.html")

def contato_view(request):
    return render(request, "contato.html")

def planos_view(request):
    return render(request, "planos.html")

def clientes_view(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        return render(request, "clientes.html", context={"clientes": clientes})
    elif request.method == "POST":
        novo_cliente = Cliente(
            nome=request.POST.get("nome"),
            telefone=request.POST.get("telefone"),
            endereco=request.POST.get("endereco"),
            cpf=request.POST.get("cpf"),
        )
        novo_cliente.save()
        return HttpResponse("Dados recebidos")

def produtos_view(request):
    if request.method == "GET":
        produtos = Produto.objects.all()
        form = ProdutoForm()
        return render(request, "produtos.html", context={"produtos": produtos, "form": form})
    elif request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("Dados recebidos")


def vendas_view(request):
    if request.method == "GET":
        vendas = Venda.objects.all()
        form = VendaForm()
        return render(request, "vendas.html", context={"vendas": vendas, "form": form})
    elif request.method == "POST":
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("Dados recebidos")

from django.db import models


class Produto(models.Model):
    nome_prod = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.nome_prod


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=200)
    cpf = models.CharField(max_length=12)
    data_nasc = models.DateField(null=True)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    anotacao = models.TextField(null=True)

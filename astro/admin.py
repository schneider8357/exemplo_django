from django.contrib import admin

# Register your models here.
from .models import Conteudo, Tema, TemaToConteudo, AssociacaoTema

admin.site.register([Conteudo, Tema, TemaToConteudo, AssociacaoTema])


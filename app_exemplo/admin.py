from django.contrib import admin

from app_exemplo.models import Produto, Cliente, Venda


admin.site.register([Produto, Cliente, Venda])

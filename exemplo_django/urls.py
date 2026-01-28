"""
URL configuration for exemplo_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app_exemplo.views import index_view, sobre_view, planos_view, contato_view, clientes_view, produtos_view, vendas_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_view),
    path("sobre", sobre_view),
    path("planos", planos_view),
    path("contato", contato_view),
    path("clientes", clientes_view),
    path("produtos", produtos_view),
    path("vendas", vendas_view),
]

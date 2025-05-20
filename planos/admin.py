from django.contrib import admin
from .models import Plano


@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'duracao_dias', 'ativo')
    list_filter = ('ativo',)

from django.contrib import admin
from .models import Pagamento


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = (
        'aluno', 'plano', 'valor', 'data_pagamento', 'status', 'metodo'
    )
    list_filter = ('status', 'metodo', 'data_pagamento')

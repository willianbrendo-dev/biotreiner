from rest_framework import serializers
from .models import Pagamento


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['id', 'aluno', 'plano', 'valor', 'data_pagamento', 'status', 'metodo']

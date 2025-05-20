from rest_framework import serializers
from .models import Plano


class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = ['id', 'nome', 'preco', 'descricao', 'duracao_dias', 'beneficios', 'ativo']

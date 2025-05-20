from rest_framework import serializers
from .models import Presenca


class PresencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenca
        fields = ['id', 'aluno', 'data_hora_entrada', 'data_hora_saida']
        read_only_fields = ['data_hora_entrada']

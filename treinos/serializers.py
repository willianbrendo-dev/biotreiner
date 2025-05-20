from rest_framework import serializers
from .models import Treino, Exercicio


class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = [
            'id', 'nome', 'grupo_muscular', 'series',
            'repeticoes', 'carga'
        ]


class TreinoSerializer(serializers.ModelSerializer):
    exercicios = ExercicioSerializer(many=True)

    class Meta:
        model = Treino
        fields = [
            'id', 'aluno', 'nome', 'gerado_por_ia',
            'data_criacao', 'observacoes', 'exercicios'
        ]

    def create(self, validated_data):
        exercicios_data = validated_data.pop('exercicios')
        treino = Treino.objects.create(**validated_data)
        for ex_data in exercicios_data:
            Exercicio.objects.create(treino=treino, **ex_data)
        return treino

    def update(self, instance, validated_data):
        exercicios_data = validated_data.pop('exercicios', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if exercicios_data:
            instance.exercicios.all().delete()  # simples substituição
            for ex_data in exercicios_data:
                Exercicio.objects.create(treino=instance, **ex_data)

        return instance

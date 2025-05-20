from django.db import models
from usuarios.models import Aluno


class Treino(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    gerado_por_ia = models.BooleanField(default=False)
    data_criacao = models.DateField(auto_now_add=True)
    observacoes = models.TextField(blank=True)


class Exercicio(models.Model):
    treino = models.ForeignKey(
        Treino,
        related_name='exercicios',
        on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=100)
    grupo_muscular = models.CharField(max_length=50)
    series = models.PositiveIntegerField()
    repeticoes = models.PositiveIntegerField()
    carga = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

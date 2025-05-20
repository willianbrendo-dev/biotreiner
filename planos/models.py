from django.db import models


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField()
    duracao_dias = models.IntegerField(default=30)
    beneficios = models.TextField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

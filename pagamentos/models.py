from django.db import models
from usuarios.models import Aluno
from planos.models import Plano


class Pagamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    plano = models.ForeignKey(Plano, on_delete=models.SET_NULL, null=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('falhou', 'Falhou')
    ], default='pendente')
    metodo = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.aluno.usuario.username} - {self.status}"

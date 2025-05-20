from django.db import models
from usuarios.models import Aluno  # ou Academia, se tiver model


class Agendamento(models.Model):
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    horario = models.DateTimeField()
    atividade = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)


class Presenca(models.Model):
    agendamento = models.ForeignKey(
        Agendamento,
        on_delete=models.CASCADE,
        related_name='presencas'
    )
    data = models.DateTimeField(auto_now_add=True)
    confirmado = models.BooleanField(default=False)

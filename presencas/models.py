from django.db import models
from usuarios.models import Aluno


class Presenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    hora_entrada = models.TimeField(auto_now_add=True)
    hora_saida = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ('aluno', 'data')  # impede múltiplas presenças no mesmo dia  # noqa

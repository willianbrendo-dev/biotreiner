from django.db import models
from academias.models import Academia
from usuarios.models import Aluno


class Agendamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    academia = models.ForeignKey(Academia, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    atividade = models.CharField(max_length=100)
    confirmado = models.BooleanField(default=False)

    class Meta:
        unique_together = ('aluno', 'data', 'horario')

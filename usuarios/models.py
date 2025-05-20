from django.contrib.auth.models import AbstractUser
from django.db import models
from academias.models import Academia
from planos.models import Plano


class Usuario(AbstractUser):
    is_aluno = models.BooleanField(default=False)
    is_academia = models.BooleanField(default=False)
    is_admin_aurevo = models.BooleanField(default=False)
    academia = models.ForeignKey(
        Academia,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


class Aluno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    plano = models.ForeignKey(
        Plano,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    data_inicio_plano = models.DateField(null=True, blank=True)
    altura = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True
    )
    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    smartwatch_sync = models.BooleanField(default=False)

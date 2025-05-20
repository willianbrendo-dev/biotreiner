from django.db import models


class Academia(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, blank=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    cor_primaria = models.CharField(max_length=7, default="#000000")

    def __str__(self):
        return self.nome

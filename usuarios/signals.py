from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario, Aluno


@receiver(post_save, sender=Usuario)
def criar_aluno_automaticamente(sender, instance, created, **kwargs):
    if (
        created
        and instance.is_aluno
        and not Aluno.objects.filter(usuario=instance).exists()
    ):
        Aluno.objects.create(usuario=instance)

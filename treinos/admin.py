from django.contrib import admin
from .models import Treino, Exercicio


class ExercicioInline(admin.TabularInline):
    model = Exercicio
    extra = 1


@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'aluno', 'gerado_por_ia', 'data_criacao')
    inlines = [ExercicioInline]


@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'treino', 'grupo_muscular', 'series', 'repeticoes', 'carga'
    )

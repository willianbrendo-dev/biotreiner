from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Aluno


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'is_aluno', 'is_academia', 'is_admin_aurevo'
    )

    def get_aluno(self, obj):
        return getattr(obj.aluno, 'id', None)

    get_aluno.short_description = 'Aluno ID'

    fieldsets = UserAdmin.fieldsets + (
        (
            'Permissões customizadas',
            {
                'fields': (
                    'is_aluno',
                    'is_academia',
                    'is_admin_aurevo',
                    'academia',
                )
            },
        ),
    )


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'plano',
        'data_inicio_plano',
        'altura',
        'peso',
        'smartwatch_sync',
    )

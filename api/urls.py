from django.urls import path, include
from rest_framework.routers import DefaultRouter

from usuarios.views import UsuarioViewSet, AlunoViewSet
from academias.views import AcademiaViewSet
from planos.views import PlanoViewSet
from treinos.views import TreinoViewSet, ExercicioViewSet
from pagamentos.views import PagamentoViewSet
from atividades.views import AgendamentoViewSet, PresencaViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'academias', AcademiaViewSet)
router.register(r'planos', PlanoViewSet)
router.register(r'treinos', TreinoViewSet)
router.register(r'exercicios', ExercicioViewSet)
router.register(r'pagamentos', PagamentoViewSet)
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'presencas', PresencaViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Autenticação (login, logout, password reset, etc)
    path('auth/', include('dj_rest_auth.urls')),

    # Registro de usuário (se quiser permitir que usuários se registrem via API)
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]

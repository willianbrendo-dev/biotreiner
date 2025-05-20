from rest_framework import viewsets
from .models import Treino, Exercicio
from .serializers import TreinoSerializer, ExercicioSerializer
from usuarios.permissions import IsAluno, IsAcademia, IsAdminAurevo


class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin_aurevo:
            return Treino.objects.all()
        elif user.is_academia:
            return Treino.objects.filter(aluno__academia=user.academia)
        elif user.is_aluno:
            return Treino.objects.filter(aluno__usuario=user)
        return Treino.objects.none()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAcademia(), IsAdminAurevo()]
        return [IsAluno(), IsAcademia(), IsAdminAurevo()]


class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
    permission_classes = [IsAcademia, IsAdminAurevo]

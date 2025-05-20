from atividades.models import Agendamento, Presenca
from rest_framework import viewsets, permissions
from .serializers import AgendamentoSerializer, PresencaSerializer


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin_aurevo:
            return Agendamento.objects.all()
        elif user.is_academia:
            return Agendamento.objects.filter(aluno__usuario__academia=user)
        elif user.is_aluno:
            return Agendamento.objects.filter(aluno__usuario=user)
        return Agendamento.objects.none()


class PresencaViewSet(viewsets.ModelViewSet):
    queryset = Presenca.objects.all()
    serializer_class = PresencaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin_aurevo:
            return Presenca.objects.all()
        elif user.is_academia:
            return Presenca.objects.filter(
                agendamento__aluno__usuario__academia=user
            )
        elif user.is_aluno:
            return Presenca.objects.filter(agendamento__aluno__usuario=user)
        return Presenca.objects.none()

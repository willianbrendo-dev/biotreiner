from rest_framework import viewsets
from .models import Presenca
from .serializers import PresencaSerializer
from rest_framework.permissions import IsAuthenticated


class PresencaViewSet(viewsets.ModelViewSet):
    queryset = Presenca.objects.all()
    serializer_class = PresencaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_admin_aurevo:
            return Presenca.objects.all()
        elif user.is_academia:
            return Presenca.objects.filter(
                aluno__usuario__academia=user.academia
            )
        elif user.is_aluno:
            return Presenca.objects.filter(aluno__usuario=user)

        return Presenca.objects.none()

    def perform_create(self, serializer):
        # Se for aluno, força o vinculo com o próprio aluno
        user = self.request.user
        if user.is_aluno:
            serializer.save(aluno=user.aluno)
        else:
            serializer.save()

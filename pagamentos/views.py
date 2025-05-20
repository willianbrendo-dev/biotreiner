from rest_framework import viewsets
from .models import Pagamento
from .serializers import PagamentoSerializer
from usuarios.permissions import IsAluno, IsAdminAurevo


class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin_aurevo:
            return Pagamento.objects.all()
        elif user.is_aluno:
            return Pagamento.objects.filter(aluno__usuario=user)
        return Pagamento.objects.none()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminAurevo()]
        return [IsAluno(), IsAdminAurevo()]

from rest_framework import viewsets
from .models import Plano
from .serializers import PlanoSerializer
from usuarios.permissions import IsAcademia, IsAdminAurevo


class PlanoViewSet(viewsets.ModelViewSet):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin_aurevo:
            return Plano.objects.all()
        elif user.is_academia:
            return Plano.objects.filter(academia=user.academia)
        return Plano.objects.none()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAcademia(), IsAdminAurevo()]
        return [IsAcademia(), IsAdminAurevo()]

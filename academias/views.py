from rest_framework import viewsets
from .models import Academia
from .serializers import AcademiaSerializer
from usuarios.permissions import IsAcademia, IsAdminAurevo


class AcademiaViewSet(viewsets.ModelViewSet):
    queryset = Academia.objects.all()
    serializer_class = AcademiaSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminAurevo()]
        return [IsAcademia(), IsAdminAurevo()]

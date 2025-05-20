from rest_framework import viewsets
from .models import Usuario, Aluno
from .serializers import UsuarioSerializer, AlunoSerializer
from usuarios.permissions import IsAluno, IsAcademia, IsAdminAurevo
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.action in ['list', 'create', 'destroy']:
            return [IsAdminAurevo()]
        return [IsAuthenticated()]


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin_aurevo:
            return Aluno.objects.all()
        elif user.is_academia:
            return Aluno.objects.filter(academia=user.academia)
        elif user.is_aluno:
            return Aluno.objects.filter(usuario=user)
        return Aluno.objects.none()

    def get_serializer_context(self):
        """Permite o uso de `self.context['request']` no serializer."""
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_permissions(self):
        """Define permissões por ação."""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAcademia(), IsAdminAurevo()]
        return [IsAluno(), IsAcademia(), IsAdminAurevo()]

    def perform_create(self, serializer):
        """Permite que o serializer use o request.user da academia criadora."""
        serializer.save()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

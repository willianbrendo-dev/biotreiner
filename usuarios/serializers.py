from rest_framework import serializers
from .models import Usuario, Aluno
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'is_aluno', 'is_academia', 'is_admin_aurevo', 'academia', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = Usuario(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class AlunoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Aluno
        fields = [
            'id', 'usuario', 'plano', 'data_inicio_plano',
            'altura', 'peso', 'smartwatch_sync', 'academia'
        ]
        read_only_fields = ['academia']

    def create(self, validated_data):
        request = self.context.get('request')
        criador = request.user if request else None

        usuario_data = validated_data.pop('usuario')
        usuario_data['is_aluno'] = True  # força o novo usuário como aluno

        usuario = UsuarioSerializer().create(usuario_data)

        # Se quem está criando for uma academia, vincula o aluno a ela
        academia = criador.academia if criador and criador.is_academia else None

        aluno = Aluno.objects.create(usuario=usuario, academia=academia, **validated_data)
        return aluno

    def update(self, instance, validated_data):
        usuario_data = validated_data.pop('usuario', None)
        if usuario_data:
            UsuarioSerializer().update(instance.usuario, usuario_data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        data.update({
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "nome": user.get_full_name(),
            "is_aluno": user.is_aluno,
            "is_academia": user.is_academia,
            "is_admin_aurevo": user.is_admin_aurevo,
        })

        if user.academia:
            data["academia_id"] = user.academia.id

        return data

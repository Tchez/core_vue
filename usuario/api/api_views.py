from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from usuario.models import Usuario

from .serializers import UsuarioGETSerializer, UsuarioSerializer


class UsuarioViewAPI(ModelViewSet):
    """Classe para gerenciar as requisições da API para POST, PUT, PATCH e DELETE"""

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.select_related().all()
    serializer_class = UsuarioSerializer


class UserHasPermissionView(APIView):
    """Endpoint para verificar se o usuário logado possui permissões especificadas.
    
    A URL deve conter o parâmetro 'perms', uma lista de nomes de permissões separados por vírgula.
    Retorna um dicionário com cada permissão e um booleano indicando se o usuário possui essa permissão.
    """

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        permissions_to_check = request.query_params.get("perms", "")

        if not permissions_to_check:
            return Response(
                {
                    "detail": "Nenhuma permissão foi informada. Informe uma ou mais permissões separadas por vírgula!",
                    "example": "/usuario/api/v1/permissions/?perms=app_name.permission_name,app_name.permission_name",
                },
                status=400,
            )

        permissions_to_check = permissions_to_check.split(",")

        if user.is_superuser:
            return Response({permission: True for permission in permissions_to_check})

        has_permissions = {
            permission: user.has_perm(permission) for permission in permissions_to_check
        }

        return Response(has_permissions)


class UsuarioCustomViewAPI(OptimizedQuerySetMixin, ReadOnlyModelViewSet):
    """Classe para gerenciar as requisições da API para o GET

    A lista filterset_fields deve ser configurada com os campos do models que poderão ser utilizados para realizar
    filtros no models como por exemplo nome_do_campo=valor_a_ser_filtrado

    A lista search_fields deve ser configurada com os campos do models que poderão ser utilizados para realizar
    buscas no models como por exemplo search=valor_a_ser_pesquisado
    """

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Usuario.objects.select_related().all()
    serializer_class = UsuarioGETSerializer
    filter_backend = [filters.SearchFilter]
    filterset_fields = []
    search_fields = []

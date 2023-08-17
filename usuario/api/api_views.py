from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
        permissions_to_check = self._get_permissions_from_request(request)

        # verifica se a lista de permissões está vazia
        if not permissions_to_check:
            return self._missing_permission_response()

        if user.is_superuser:
            return Response({permission: True for permission in permissions_to_check})

        return Response(self._check_user_permissions(user, permissions_to_check))

    def _get_permissions_from_request(self, request) -> list:
        """
        Extrai as permissões dos parâmetros de consulta da solicitação.
        """
        params = request.query_params.get("perms", "")
        return params.split(",") if params else []

    def _missing_permission_response(self):
        """
        Resposta quando o parâmetro 'perms' não é fornecido na solicitação.
        """
        return Response(
            {
                "detail": "Nenhuma permissão foi informada. Informe uma ou mais permissões separadas por vírgula!",
                "example": "/usuario/api/v1/permissions/?perms=app_name.permission_name,app_name.permission_name",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def _check_user_permissions(self, user, permissions_to_check):
        """
        Check which permissions the user has from the provided list.
        """
        return {
            permission: user.has_perm(permission) for permission in permissions_to_check
        }


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

from rest_framework import routers
from django.urls import path

from .api_views import UsuarioCustomViewAPI, UsuarioViewAPI, UserHasPermissionView

router = routers.DefaultRouter()

# URL para a API Usuario
router.register(r"usuario", UsuarioViewAPI, "usuario-api")
router.register(r"usuario/custom", UsuarioCustomViewAPI, "usuario-get-api")

# Definir views baseadas em APIView manualmente
urlpatterns = [
    path("permissions/", UserHasPermissionView.as_view(), name="user-permissions"),
]

# Adicionar as URLs registradas pelo router
urlpatterns += router.urls

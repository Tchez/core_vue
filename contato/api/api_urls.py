from rest_framework import routers

from .api_views import ContatoCustomViewAPI, ContatoViewAPI

router = routers.DefaultRouter()

# URL para a API Contato
router.register(r"contato", ContatoViewAPI, "contato-api")
router.register(r"contato/custom", ContatoCustomViewAPI, "contato-get-api")

urlpatterns = router.urls

from rest_framework import routers

from .api_views import (
    AlunoCustomViewAPI,
    AlunoViewAPI,
    CursoCustomViewAPI,
    CursoViewAPI,
)

router = routers.DefaultRouter()

# URL para a API Curso
router.register(r"curso", CursoViewAPI, "curso-api")
router.register(r"curso/custom", CursoCustomViewAPI, "curso-get-api")


# URL para a API Aluno
router.register(r"aluno", AlunoViewAPI, "aluno-api")
router.register(r"aluno/custom", AlunoCustomViewAPI, "aluno-get-api")

urlpatterns = router.urls

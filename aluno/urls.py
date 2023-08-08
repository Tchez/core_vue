from django.urls import path

from .views import (
    AlunoCreateView,
    AlunoDeleteView,
    AlunoDetailView,
    AlunoIndexTemplateView,
    AlunoListView,
    AlunoRestoreView,
    AlunoUpdateView,
    CursoCreateView,
    CursoDeleteView,
    CursoDetailView,
    CursoListView,
    CursoRestoreView,
    CursoUpdateView,
)

app_name = "aluno"

# URLs do Models Curso
urlpatterns = [
    path("aluno/", AlunoIndexTemplateView.as_view(), name="aluno-index"),
    path("aluno/curso/", CursoListView.as_view(), name="curso-list"),
    path("aluno/curso/create/", CursoCreateView.as_view(), name="curso-create"),
    path("aluno/curso/<uuid:pk>/", CursoDetailView.as_view(), name="curso-detail"),
    path(
        "aluno/curso/update/<uuid:pk>/", CursoUpdateView.as_view(), name="curso-update"
    ),
    path(
        "aluno/curso/delete/<uuid:pk>/", CursoDeleteView.as_view(), name="curso-delete"
    ),
    path(
        "aluno/curso/restore/<uuid:pk>/",
        CursoRestoreView.as_view(),
        name="curso-restore",
    ),
]


# URLs do Models Aluno
urlpatterns += [
    path("aluno/", AlunoIndexTemplateView.as_view(), name="aluno-index"),
    path("aluno/aluno/", AlunoListView.as_view(), name="aluno-list"),
    path("aluno/aluno/create/", AlunoCreateView.as_view(), name="aluno-create"),
    path("aluno/aluno/<uuid:pk>/", AlunoDetailView.as_view(), name="aluno-detail"),
    path(
        "aluno/aluno/update/<uuid:pk>/", AlunoUpdateView.as_view(), name="aluno-update"
    ),
    path(
        "aluno/aluno/delete/<uuid:pk>/", AlunoDeleteView.as_view(), name="aluno-delete"
    ),
    path(
        "aluno/aluno/restore/<uuid:pk>/",
        AlunoRestoreView.as_view(),
        name="aluno-restore",
    ),
]

from aluno.forms import CursoForm
from aluno.models import Curso
from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)


# Views do Models Curso
class CursoListView(BaseListView):
    """Classe para gerenciar a listagem do Curso"""

    model = Curso
    template_name = "aluno/curso/curso_list.html"
    context_object_name = "curso"

    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CursoListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        if self.request.user.is_superuser:
            queryset = super(CursoListView, self).get_queryset()
            return queryset
        else:
            queryset = super(CursoListView, self).get_queryset()
            return queryset


class CursoDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do Curso"""

    model = Curso
    form_class = CursoForm
    success_url = "aluno:curso-list"
    template_name = "aluno/curso/curso_detail.html"
    context_object_name = "curso"

    def get_context_data(self, **kwargs):
        context = super(CursoDetailView, self).get_context_data(**kwargs)
        return context


class CursoCreateView(BaseCreateView):
    """Classe para gerenciar o create do Curso"""

    model = Curso
    form_class = CursoForm
    context_object_name = "curso"
    success_url = "aluno:curso-list"
    template_name = "aluno/curso/curso_create.html"
    # inlines = []


class CursoUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do Curso"""

    model = Curso
    form_class = CursoForm
    context_object_name = "curso"
    success_url = "aluno:curso-list"
    template_name = "aluno/curso/curso_update.html"
    # inlines = []


class CursoDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do Curso"""

    model = Curso
    form_class = CursoForm
    context_object_name = "curso"
    success_url = "aluno:curso-list"
    template_name = "aluno/curso/curso_delete.html"


class CursoRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do Curso"""

    model = Curso
    context_object_name = "curso"
    success_url = "aluno:curso-list"
    template_name = "aluno/curso/curso_restore.html"


# Fim das Views do Models Curso

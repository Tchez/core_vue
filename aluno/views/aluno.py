from aluno.forms import AlunoForm, CursoForm, ContatoFormSet
from aluno.models import Aluno
from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)
from contato.models import Contato


# Views do Models Aluno
class AlunoListView(BaseListView):
    """Classe para gerenciar a listagem do Aluno"""

    model = Aluno
    template_name = "aluno/aluno/aluno_list.html"
    context_object_name = "aluno"
    list_display = ["nome", "matricula", "curso", "ativo"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(AlunoListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        if self.request.user.is_superuser:
            queryset = super(AlunoListView, self).get_queryset()
            return queryset
        else:
            queryset = super(AlunoListView, self).get_queryset()
            return queryset


class AlunoDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do Aluno"""

    model = Aluno
    form_class = AlunoForm
    success_url = "aluno:aluno-list"
    template_name = "aluno/aluno/aluno_detail.html"
    context_object_name = "aluno"

    def get_context_data(self, **kwargs):
        context = super(AlunoDetailView, self).get_context_data(**kwargs)
        return context


class AlunoCreateView(BaseCreateView):
    """Classe para gerenciar o create do Aluno"""

    model = Aluno
    form_class = AlunoForm
    context_object_name = "aluno"
    success_url = "aluno:aluno-list"
    template_name = "aluno/aluno/aluno_create.html"
    inlines = [
        ContatoFormSet,
    ]

    def get_context_data(self, **kwargs):
        context = super(AlunoCreateView, self).get_context_data(**kwargs)
        context["form_curso"] = CursoForm
        return context


class AlunoUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do Aluno"""

    model = Aluno
    form_class = AlunoForm
    context_object_name = "aluno"
    success_url = "aluno:aluno-list"
    template_name = "aluno/aluno/aluno_update.html"
    # inlines = []

    def get_context_data(self, **kwargs):
        context = super(AlunoUpdateView, self).get_context_data(**kwargs)
        context["form_curso"] = CursoForm
        return context


class AlunoDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do Aluno"""

    model = Aluno
    form_class = AlunoForm
    context_object_name = "aluno"
    success_url = "aluno:aluno-list"
    template_name = "aluno/aluno/aluno_delete.html"


class AlunoRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do Aluno"""

    model = Aluno
    context_object_name = "aluno"
    success_url = "aluno:aluno-list"
    template_name = "aluno/aluno/aluno_restore.html"


# Fim das Views do Models Aluno

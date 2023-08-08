from contato.forms import ContatoForm
from contato.models import Contato
from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)


# Views do Models Contato
class ContatoListView(BaseListView):
    """Classe para gerenciar a listagem do Contato"""

    model = Contato
    template_name = "contato/contato/contato_list.html"
    context_object_name = "contato"
    list_display = ["tipo_contato", "valor"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ContatoListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        if self.request.user.is_superuser:
            queryset = super(ContatoListView, self).get_queryset()
            return queryset
        else:
            queryset = super(ContatoListView, self).get_queryset()
            return queryset


class ContatoDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do Contato"""

    model = Contato
    form_class = ContatoForm
    success_url = "contato:contato-list"
    template_name = "contato/contato/contato_detail.html"
    context_object_name = "contato"

    def get_context_data(self, **kwargs):
        context = super(ContatoDetailView, self).get_context_data(**kwargs)
        return context


class ContatoCreateView(BaseCreateView):
    """Classe para gerenciar o create do Contato"""

    model = Contato
    form_class = ContatoForm
    context_object_name = "contato"
    success_url = "contato:contato-list"
    template_name = "contato/contato/contato_create.html"
    # inlines = []


class ContatoUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do Contato"""

    model = Contato
    form_class = ContatoForm
    context_object_name = "contato"
    success_url = "contato:contato-list"
    template_name = "contato/contato/contato_update.html"
    # inlines = []


class ContatoDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do Contato"""

    model = Contato
    form_class = ContatoForm
    context_object_name = "contato"
    success_url = "contato:contato-list"
    template_name = "contato/contato/contato_delete.html"


class ContatoRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do Contato"""

    model = Contato
    context_object_name = "contato"
    success_url = "contato:contato-list"
    template_name = "contato/contato/contato_restore.html"


# Fim das Views do Models Contato

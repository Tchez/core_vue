from core.views.base import BaseTemplateView


# Views Inicial Aluno
class AlunoIndexTemplateView(BaseTemplateView):
    # Views para renderizar a tela inicial Aluno
    template_name = "aluno/index.html"
    context_object_name = "aluno"

    def get_context_data(self, **kwargs):
        context = super(AlunoIndexTemplateView, self).get_context_data(**kwargs)
        return context

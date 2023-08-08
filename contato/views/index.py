from core.views.base import BaseTemplateView


# Views Inicial Contato
class ContatoIndexTemplateView(BaseTemplateView):
    # Views para renderizar a tela inicial Contato
    template_name = "contato/index.html"
    context_object_name = "contato"

    def get_context_data(self, **kwargs):
        context = super(ContatoIndexTemplateView, self).get_context_data(**kwargs)
        return context

from core.forms import BaseForm

from .models import Contato


class ContatoForm(BaseForm):
    """Form padrão para o model Contato"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = Contato

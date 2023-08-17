from django.forms import inlineformset_factory

from contato.forms import ContatoForm
from contato.models import Contato
from core.forms import BaseForm

from .models import Aluno, Curso


class CursoForm(BaseForm):
    """Form padrão para o model Curso"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = Curso


class AlunoForm(BaseForm):
    """Form padrão para o model Aluno"""

    class Meta:
        exclude = ["deleted",]
        model = Aluno


ContatoFormSet = inlineformset_factory(Aluno, Contato, form=ContatoForm, extra=1)

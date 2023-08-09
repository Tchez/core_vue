from core.forms import BaseForm

from django.forms import inlineformset_factory

from .models import Aluno, Curso
from contato.models import Contato
from contato.forms import ContatoForm


class CursoForm(BaseForm):
    """Form padrão para o model Curso"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = Curso


class AlunoForm(BaseForm):
    """Form padrão para o model Aluno"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = Aluno


ContatoFormSet = inlineformset_factory(Aluno, Contato, form=ContatoForm, extra=1)

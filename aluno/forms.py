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
        exclude = ["deleted", "enabled"]
        model = Aluno

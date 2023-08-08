import pytest
from faker import Faker

from aluno.forms import CursoForm


class TestCursoForms:
    """Testes para os formulários de Curso"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_curso_create(self, init):
        """Teste para criação de Curso"""
        form = CursoForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_curso_form_invalid(self, init):
        """Teste para formulário inválido de Curso"""
        form = CursoForm(data=self.invalid_data)
        assert form.is_valid() is False

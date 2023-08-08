import pytest
from faker import Faker

from aluno.forms import AlunoForm


class TestAlunoForms:
    """Testes para os formulários de Aluno"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_aluno_create(self, init):
        """Teste para criação de Aluno"""
        form = AlunoForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_aluno_form_invalid(self, init):
        """Teste para formulário inválido de Aluno"""
        form = AlunoForm(data=self.invalid_data)
        assert form.is_valid() is False

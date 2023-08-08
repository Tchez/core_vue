import pytest
from faker import Faker

from contato.forms import ContatoForm


class TestContatoForms:
    """Testes para os formulários de Contato"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_contato_create(self, init):
        """Teste para criação de Contato"""
        form = ContatoForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_contato_form_invalid(self, init):
        """Teste para formulário inválido de Contato"""
        form = ContatoForm(data=self.invalid_data)
        assert form.is_valid() is False

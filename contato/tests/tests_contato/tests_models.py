import pytest
from faker import Faker
from model_bakery import baker

from contato.models import Contato


class TestContatoModels:
    """Testes para o model Contato"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.contato = baker.make(Contato)

    def test_count_contato(self, init):
        """Testa a quantidade de contato"""
        assert Contato.objects.all().count() == 1

    def test_soft_delete_contato(self, init):
        """Testa o soft delete de contato"""
        Contato.objects.all().delete()
        assert Contato.objects.filter(deleted=False).count() == 0

    def test_create_contato(self, init):
        """Testa a criação de contato"""
        assert self.contato.id is not None

    def test_update_contato(self, init):
        """Testa a atualização de contato"""
        # TODO - Altere o campo e o valor
        self.contato.save()
        self.contato.campo = "valor"
        self.contato.save()
        contato = Contato.objects.get(campo="valor")
        assert contato.campo == "valor"

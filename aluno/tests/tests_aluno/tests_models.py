import pytest
from faker import Faker
from model_bakery import baker

from aluno.models import Aluno


class TestAlunoModels:
    """Testes para o model Aluno"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.aluno = baker.make(Aluno)

    def test_count_aluno(self, init):
        """Testa a quantidade de aluno"""
        assert Aluno.objects.all().count() == 1

    def test_soft_delete_aluno(self, init):
        """Testa o soft delete de aluno"""
        Aluno.objects.all().delete()
        assert Aluno.objects.filter(deleted=False).count() == 0

    def test_create_aluno(self, init):
        """Testa a criação de aluno"""
        assert self.aluno.id is not None

    def test_update_aluno(self, init):
        """Testa a atualização de aluno"""
        # TODO - Altere o campo e o valor
        self.aluno.save()
        self.aluno.campo = "valor"
        self.aluno.save()
        aluno = Aluno.objects.get(campo="valor")
        assert aluno.campo == "valor"

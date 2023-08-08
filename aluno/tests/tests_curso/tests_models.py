import pytest
from faker import Faker
from model_bakery import baker

from aluno.models import Curso


class TestCursoModels:
    """Testes para o model Curso"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.curso = baker.make(Curso)

    def test_count_curso(self, init):
        """Testa a quantidade de curso"""
        assert Curso.objects.all().count() == 1

    def test_soft_delete_curso(self, init):
        """Testa o soft delete de curso"""
        Curso.objects.all().delete()
        assert Curso.objects.filter(deleted=False).count() == 0

    def test_create_curso(self, init):
        """Testa a criação de curso"""
        assert self.curso.id is not None

    def test_update_curso(self, init):
        """Testa a atualização de curso"""
        # TODO - Altere o campo e o valor
        self.curso.save()
        self.curso.campo = "valor"
        self.curso.save()
        curso = Curso.objects.get(campo="valor")
        assert curso.campo == "valor"

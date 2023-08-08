import pytest
from django.contrib.auth.models import User
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import RequestFactory
from django.urls import reverse
from faker import Faker
from model_bakery import baker

from aluno.models import Curso
from aluno.views import (
    AlunoIndexTemplateView,
    CursoCreateView,
    CursoDeleteView,
    CursoDetailView,
    CursoListView,
    CursoUpdateView,
)


class TestCursoViews:
    """Teste para as views do model Curso"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="teste",
            email="teste@email.com.br",
            password="senha_padrao_deve_ser_mudada",
        )
        self.curso = baker.make(Curso)

    def test_curso_list(self, init):
        """Teste para a view list."""
        url = reverse("aluno:curso-list")
        request = self.factory.get(url)
        request.user = self.user
        response = CursoListView.as_view()(request)
        assert response.status_code == 200

    def test_curso_detail(self, init):
        """Teste para a view detail."""
        url = reverse("aluno:curso-detail", args={self.curso.pk})
        request = self.factory.get(url)
        request.user = self.user
        response = CursoDetailView.as_view()(request, pk=self.curso.pk)
        assert response.status_code == 200

    def test_curso_create(self, init):
        """Teste para a view create."""
        url = reverse("aluno:curso-create")
        request = self.factory.get(url)
        request.user = self.user
        response = CursoCreateView.as_view()(request)
        assert response.status_code == 200

    def test_curso_create_post(self, init):
        """Teste para a view create usando Post."""

        # TODO - Adicione campos
        data = {}
        url = reverse("aluno:curso-create")
        request = self.factory.post(url)
        request.user = self.user
        response = CursoCreateView.as_view()(request, data=data)
        assert response.status_code == 200

    def test_curso_update(self, init):
        """Teste para a view update."""
        url = reverse("aluno:curso-update", args={self.curso.pk})
        request = self.factory.put(url)
        request.user = self.user
        response = CursoUpdateView.as_view()(request, pk=self.curso.pk)
        assert response.status_code == 200

    def test_curso_delete(self, init):
        """Teste para a view delete."""
        url = reverse("aluno:curso-delete", args={self.curso.pk})
        request = self.factory.delete(url)
        setattr(request, "session", "session")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        request.user = self.user
        response = CursoDeleteView.as_view()(request, pk=self.curso.pk)
        mensagem = list(messages)[0].extra_tags
        assert mensagem == "success"
        assert response.status_code == 302

    def test_curso_queryset_superuser_status(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("aluno:curso-list"))
        request.user = self.user
        response = CursoListView.as_view()(request)
        assert response.status_code == 200

    def test_curso_queryset_superuser(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("aluno:curso-list"))
        request.user = self.user
        response = CursoListView.as_view()(request)
        assert len(response.context_data["object_list"]) == 1

    def test_aluno_index(self, init):
        """Teste para a view index."""
        url = reverse("aluno:aluno-index")
        request = self.factory.get(url)
        request.user = self.user
        response = AlunoIndexTemplateView.as_view()(request)
        assert response.status_code == 200

import pytest
from django.contrib.auth.models import User
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import RequestFactory
from django.urls import reverse
from faker import Faker
from model_bakery import baker

from aluno.models import Aluno
from aluno.views import (
    AlunoCreateView,
    AlunoDeleteView,
    AlunoDetailView,
    AlunoIndexTemplateView,
    AlunoListView,
    AlunoUpdateView,
)


class TestAlunoViews:
    """Teste para as views do model Aluno"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="teste",
            email="teste@email.com.br",
            password="senha_padrao_deve_ser_mudada",
        )
        self.aluno = baker.make(Aluno)

    def test_aluno_list(self, init):
        """Teste para a view list."""
        url = reverse("aluno:aluno-list")
        request = self.factory.get(url)
        request.user = self.user
        response = AlunoListView.as_view()(request)
        assert response.status_code == 200

    def test_aluno_detail(self, init):
        """Teste para a view detail."""
        url = reverse("aluno:aluno-detail", args={self.aluno.pk})
        request = self.factory.get(url)
        request.user = self.user
        response = AlunoDetailView.as_view()(request, pk=self.aluno.pk)
        assert response.status_code == 200

    def test_aluno_create(self, init):
        """Teste para a view create."""
        url = reverse("aluno:aluno-create")
        request = self.factory.get(url)
        request.user = self.user
        response = AlunoCreateView.as_view()(request)
        assert response.status_code == 200

    def test_aluno_create_post(self, init):
        """Teste para a view create usando Post."""

        # TODO - Adicione campos
        data = {}
        url = reverse("aluno:aluno-create")
        request = self.factory.post(url)
        request.user = self.user
        response = AlunoCreateView.as_view()(request, data=data)
        assert response.status_code == 200

    def test_aluno_update(self, init):
        """Teste para a view update."""
        url = reverse("aluno:aluno-update", args={self.aluno.pk})
        request = self.factory.put(url)
        request.user = self.user
        response = AlunoUpdateView.as_view()(request, pk=self.aluno.pk)
        assert response.status_code == 200

    def test_aluno_delete(self, init):
        """Teste para a view delete."""
        url = reverse("aluno:aluno-delete", args={self.aluno.pk})
        request = self.factory.delete(url)
        setattr(request, "session", "session")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        request.user = self.user
        response = AlunoDeleteView.as_view()(request, pk=self.aluno.pk)
        mensagem = list(messages)[0].extra_tags
        assert mensagem == "success"
        assert response.status_code == 302

    def test_aluno_queryset_superuser_status(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("aluno:aluno-list"))
        request.user = self.user
        response = AlunoListView.as_view()(request)
        assert response.status_code == 200

    def test_aluno_queryset_superuser(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("aluno:aluno-list"))
        request.user = self.user
        response = AlunoListView.as_view()(request)
        assert len(response.context_data["object_list"]) == 1

    def test_aluno_index(self, init):
        """Teste para a view index."""
        url = reverse("aluno:aluno-index")
        request = self.factory.get(url)
        request.user = self.user
        response = AlunoIndexTemplateView.as_view()(request)
        assert response.status_code == 200

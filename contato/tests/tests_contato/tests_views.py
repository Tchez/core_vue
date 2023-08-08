import pytest
from django.contrib.auth.models import User
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import RequestFactory
from django.urls import reverse
from faker import Faker
from model_bakery import baker

from contato.models import Contato
from contato.views import (
    ContatoCreateView,
    ContatoDeleteView,
    ContatoDetailView,
    ContatoIndexTemplateView,
    ContatoListView,
    ContatoUpdateView,
)


class TestContatoViews:
    """Teste para as views do model Contato"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="teste",
            email="teste@email.com.br",
            password="senha_padrao_deve_ser_mudada",
        )
        self.contato = baker.make(Contato)

    def test_contato_list(self, init):
        """Teste para a view list."""
        url = reverse("contato:contato-list")
        request = self.factory.get(url)
        request.user = self.user
        response = ContatoListView.as_view()(request)
        assert response.status_code == 200

    def test_contato_detail(self, init):
        """Teste para a view detail."""
        url = reverse("contato:contato-detail", args={self.contato.pk})
        request = self.factory.get(url)
        request.user = self.user
        response = ContatoDetailView.as_view()(request, pk=self.contato.pk)
        assert response.status_code == 200

    def test_contato_create(self, init):
        """Teste para a view create."""
        url = reverse("contato:contato-create")
        request = self.factory.get(url)
        request.user = self.user
        response = ContatoCreateView.as_view()(request)
        assert response.status_code == 200

    def test_contato_create_post(self, init):
        """Teste para a view create usando Post."""

        # TODO - Adicione campos
        data = {}
        url = reverse("contato:contato-create")
        request = self.factory.post(url)
        request.user = self.user
        response = ContatoCreateView.as_view()(request, data=data)
        assert response.status_code == 200

    def test_contato_update(self, init):
        """Teste para a view update."""
        url = reverse("contato:contato-update", args={self.contato.pk})
        request = self.factory.put(url)
        request.user = self.user
        response = ContatoUpdateView.as_view()(request, pk=self.contato.pk)
        assert response.status_code == 200

    def test_contato_delete(self, init):
        """Teste para a view delete."""
        url = reverse("contato:contato-delete", args={self.contato.pk})
        request = self.factory.delete(url)
        setattr(request, "session", "session")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        request.user = self.user
        response = ContatoDeleteView.as_view()(request, pk=self.contato.pk)
        mensagem = list(messages)[0].extra_tags
        assert mensagem == "success"
        assert response.status_code == 302

    def test_contato_queryset_superuser_status(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("contato:contato-list"))
        request.user = self.user
        response = ContatoListView.as_view()(request)
        assert response.status_code == 200

    def test_contato_queryset_superuser(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("contato:contato-list"))
        request.user = self.user
        response = ContatoListView.as_view()(request)
        assert len(response.context_data["object_list"]) == 1

    def test_contato_index(self, init):
        """Teste para a view index."""
        url = reverse("contato:contato-index")
        request = self.factory.get(url)
        request.user = self.user
        response = ContatoIndexTemplateView.as_view()(request)
        assert response.status_code == 200

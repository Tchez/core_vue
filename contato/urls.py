from django.urls import path

from .views import (
    ContatoCreateView,
    ContatoDeleteView,
    ContatoDetailView,
    ContatoIndexTemplateView,
    ContatoListView,
    ContatoRestoreView,
    ContatoUpdateView,
)

app_name = "contato"

# URLs do Models Contato
urlpatterns = [
    path("contato/", ContatoIndexTemplateView.as_view(), name="contato-index"),
    path("contato/contato/", ContatoListView.as_view(), name="contato-list"),
    path("contato/contato/create/", ContatoCreateView.as_view(), name="contato-create"),
    path(
        "contato/contato/<uuid:pk>/", ContatoDetailView.as_view(), name="contato-detail"
    ),
    path(
        "contato/contato/update/<uuid:pk>/",
        ContatoUpdateView.as_view(),
        name="contato-update",
    ),
    path(
        "contato/contato/delete/<uuid:pk>/",
        ContatoDeleteView.as_view(),
        name="contato-delete",
    ),
    path(
        "contato/contato/restore/<uuid:pk>/",
        ContatoRestoreView.as_view(),
        name="contato-restore",
    ),
]

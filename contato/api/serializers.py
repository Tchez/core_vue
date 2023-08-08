from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from contato.models import Contato


class ContatoSerializer(ModelSerializer):
    """Class do serializer do model Contato para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = Contato
        exclude = ["deleted", "enabled"]


class ContatoGETSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model Contato para o GET"""

    class Meta:
        model = Contato
        exclude = ["deleted", "enabled"]

from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from aluno.models import Aluno, Curso


class CursoSerializer(ModelSerializer):
    """Class do serializer do model Curso para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = Curso
        exclude = ["deleted", "enabled"]


class CursoGETSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model Curso para o GET"""

    class Meta:
        model = Curso
        exclude = ["deleted", "enabled"]


class AlunoSerializer(ModelSerializer):
    """Class do serializer do model Aluno para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = Aluno
        exclude = ["deleted", "enabled"]


class AlunoGETSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model Aluno para o GET"""

    class Meta:
        model = Aluno
        exclude = ["deleted", "enabled"]

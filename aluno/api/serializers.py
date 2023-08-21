from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer, SerializerMethodField, StringRelatedField

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


class AlunoListSerializer(ModelSerializer):
    """Classe para gerenciar as requisições da API para o GET"""

    curso = StringRelatedField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.idade = SerializerMethodField()
        self.fields["idade"] = self.idade

    def get_idade(self, obj):
        return obj.pegar_idade_aluno()

    class Meta:
        model = Aluno
        fields = "__all__"


class AlunoGETSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model Aluno para o GET"""

    class Meta:
        model = Aluno
        exclude = ["deleted", "enabled"]

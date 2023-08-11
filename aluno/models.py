from datetime import datetime

from django.db import models

from core.models import Base


class Curso(Base):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        fields_display = [
            "nome",
            "descricao",
        ]


class Aluno(Base):
    nome = models.CharField("Nome", max_length=100)
    data_nascimento = models.DateField("Data de nascimento")
    matricula = models.CharField("Matrícula", max_length=255)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def pegar_idade_aluno(self) -> int:
        """Método para retornar a idade do aluno com base na data de nascimento.
        Returns:
            int: idade do aluno
        """
        return int((datetime.now().date() - self.data_nascimento).days / 365.25)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        fields_display = [
            "nome",
            "matricula",
            "curso",
            "ativo",
        ]
        fk_fields_modal = [
            "curso",
        ]

from django.db import models
from core.models import Base
from aluno.models import Aluno


class Contato(Base):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    tipo_contato = models.CharField("Tipo de Contato", max_length=50)
    valor = models.CharField("Contato", max_length=255)

    def __str__(self):
        return f"{self.tipo_contato}: {self.valor}"

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        fields_display = [
            "tipo_contato",
            "valor",
        ]

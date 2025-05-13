from django.db import models
from .estado import Estado

class Cidade(models.Model):
    class Meta:
        db_table = 'cidades'

    id = models.AutoField(primary_key=True)
    nome = models.CharField(
        'Nome da Cidade',
        max_length=100,
        null=False,
        blank=False
    )
    estado = models.ForeignKey(
        to=Estado,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.nome} ({self.estado.sigla})'
from django.db import models

class Cidade(models.Model):
    class Meta:
        db_table = 'cidades'

    id = models.AutoField(primary_key=True)
    nome = models.CharField(
        'Nome da Cidade',
        max_length=100,
        null=False,
        blank=False,
    )

    def __str__(self):
        return {self.nome}
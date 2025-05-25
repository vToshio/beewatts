from django.db import models

class Marca(models.Model):
    class Meta:
        db_table = 'marcas'

    id = models.AutoField(primary_key=True)
    nome = models.CharField(
        'Nome',
        unique=True,
        max_length=30,
        null=False,
        blank=True
    )

    def __str__(self):
        return self.nome
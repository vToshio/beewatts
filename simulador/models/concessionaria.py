from django.db import models
from simulador.validators import validar_positivo

class Concessionaria(models.Model):
    class Meta:
        db_table = 'concessionarias'

    id = models.AutoField(primary_key=True)
    nome = models.CharField(
        'Nome da Concessionária',
        unique=True,
        max_length=100,
        null=False,
        blank=False
    )
    tarifa = models.FloatField(
        'Valor da Tarifa (R$)',
        validators=[
            validar_positivo,
        ],   
        null=False,
        blank=False
    )

    def __str__(self):
        return self.nome
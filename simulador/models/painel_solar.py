from django.db import models
from simulador.validators import validar_positivo
from datetime import date

class PainelSolar(models.Model):
    class Meta:
        db_table = 'paineis_solares'

    id = models.AutoField(primary_key=True)
    nome = models.CharField(
        'Nome do Painel',
        unique=True,
        max_length=50,
        null=True,
        blank=True,
    )
    valor = models.FloatField(
        'Valor (R$)', 
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False
    )   
    potencia = models.FloatField(
        'Potência (W)',
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False
    )
    altura = models.FloatField(
        'Altura (m)',
        validators=[
            validar_positivo,
        ],
        null = False,
        blank=False
    )
    largura = models.FloatField(
        'Largura (m)',
        validators=[
            validar_positivo,
        ],
        null = False,
        blank=False
    )
    data_consulta = models.DateField(
        'Data de Consulta',
        null=True,
        blank=True,
        default=date.today
    )
    link = models.URLField(
        'Link de Referência',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        self.nome = f'{int(self.potencia)} W'
        self.data_consulta = date.today()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nome
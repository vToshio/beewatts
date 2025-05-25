from django.db import models
from simulador.validators import validar_positivo
from datetime import date

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
    te = models.FloatField(
        'Tarifa TE (R$)',
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False,
    )
    tusd = models.FloatField(
        'Tarifa TUSD (R$)',
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False,
    )
    atualizada_em = models.DateField(
        'Atualizada em',
        default=date.today,
        null=False,
        blank=False
    )

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
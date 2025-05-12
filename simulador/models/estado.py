from django.db import models

class Estado(models.Model):
    class Meta:
        db_table = 'estados'
    
    id = models.AutoField(primary_key=True)
    sigla = models.CharField(
        'Sigla do Estado',
        max_length=2,
        unique=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.sigla


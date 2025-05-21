from django.core.exceptions import ValidationError

def validar_positivo(valor: float|int):
    if (valor <= 0):
        raise ValidationError(
            message='O valor precisa ser positivo!'
        )
    
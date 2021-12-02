import random

from django.db import models

from cadastro.models import Cadastro


def num_aleatorio():
    return random.randint(100000, 999999)


class Conta(models.Model):
    cadastro = models.OneToOneField(
        Cadastro,
        on_delete=models.CASCADE
    )
    agencia = models.CharField(max_length=5, default=12345)
    numero_conta = models.IntegerField(
        unique=True, null=False, default=num_aleatorio)
    saldo = models.PositiveIntegerField(default=500)

from uuid import uuid4

from django.db import models

from cadastro.models import Cadastro


class Conta(models.Model):
    cadastro = models.ForeignKey(
        Cadastro,
        on_delete=models.CASCADE
    )
    agencia = models.CharField(max_length=5,default=12345)
    numero_conta = models.UUIDField(default=uuid4)
    saldo_inicial = models.PositiveIntegerField(default=500)

    def __str__(self) -> int():
        return self.numero_conta

from django.db import models
from cadastro.models import Cadastro
from conta.models import Conta


# Create your models here.

class Transacao(models.Model):
    cadastro = models.OneToOneField(
        Cadastro, on_delete=models.CASCADE)
    entrada_nome = models.CharField(Cadastro, max_length=150, default=None)
    numero_conta_destino = models.IntegerField()
    valor_para_transferencia = models.IntegerField()

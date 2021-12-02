from django.db import models
from django.db.models.fields import Field
from cadastro.models import Cadastro
from conta.models import Conta
from django.db.models import Model
from datetime import datetime


class Transacao(models.Model):
    remetente = models.ForeignKey(
        Conta, on_delete=models.DO_NOTHING, related_name='remetente')
    destinatario = models.ForeignKey(
        Conta,  on_delete=models.DO_NOTHING, related_name='destinatario')
    data = models.DateTimeField(auto_now=True)
    valor_transferido = models.PositiveIntegerField()

from .models import Transacao
from rest_framework import serializers


class TransferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['id', 'remetente',
                  'destinatario', 'valor_transferido', 'data']

from .models import Transacao
from rest_framework import serializers


class TransferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['id', 'entrada_nome',
                  'numero_conta_destino', 'valor_para_transferencia']

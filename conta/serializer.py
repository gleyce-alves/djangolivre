from .models import Conta
from rest_framework import serializers

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id', 'agencia', 'numero_conta', 'saldo', 'cadastro']
        read_only_fields = ('numero_conta', 'agencia')

from rest_framework.exceptions import ValidationError

from .models import Conta
from rest_framework import serializers

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id', 'agencia', 'numero_conta', 'saldo', 'cadastro']
        read_only_fields = ('numero_conta', 'agencia')

    def validate_saldo(self, value):
        if value < 500:
            raise ValidationError("Saldo inicial deve ser maior que 500")
        return value
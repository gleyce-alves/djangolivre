from django import forms
from . import models


class FormularioCadastro (forms.ModelForm):
    class Meta:
        model = models.Cadastro
        fields = ["nome_completo", "cpf", "rg",
                  "endereco", "telefone_de_contato", "email"]


class FormularioConta (forms.ModelForm):
    class Meta:
        model = models.Conta
        fields = ["agencia", "numero_conta", "saldo"]


class FormularioTransacao (forms.ModelForm):
    class Meta:
        model = models.Transacao
        fields = [
            "remetente",
            "destinatario",
            "data",
            "valor_transferido
        ]

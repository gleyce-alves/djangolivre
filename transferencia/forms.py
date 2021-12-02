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
            "entrada_nome",
            "numero_conta_destino",
            "valor_para_transferencia",
            "cadastro"
        ]

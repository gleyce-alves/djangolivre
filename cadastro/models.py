from django.db import models

# Importe a classe que apresentará um erro de validação

from django.core.exceptions import ValidationError

# Crie um método para validar o valor informado

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('O CPF deve conter apenas números')

def validate_Rg(value):
    if not value.isdigit():
        raise ValidationError('O Rg deve conter apenas números')

def validate_telefone_de_contato(value):
    if not value.isdigit():
        raise ValidationError('O telefone deve conter apenas números')

class Cadastro(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, validators=[validate_cpf])
    rg = models.CharField(max_length=9, validators=[validate_Rg])
    endereco = models.CharField(max_length=100)
    telefone_de_contato = models.CharField(max_length=11, validators=[validate_telefone_de_contato])
    email = models.EmailField(max_length=50, verbose_name="email")

    # def __str__(self) -> str:
    #   return self.name

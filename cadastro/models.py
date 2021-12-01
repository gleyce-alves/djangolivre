from django.db import models


class Cadastro(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    endereco = models.CharField(max_length=100)
    telefone_de_contato = models.CharField(max_length=11)
    email = models.EmailField(max_length=50, verbose_name="email")

    # def __str__(self) -> str:
    #   return self.name

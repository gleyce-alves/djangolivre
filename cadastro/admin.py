from django.contrib import admin
from cadastro.models import Cadastro

class CadastroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'cpf', 'rg', 'endereco', 'telefone_de_contato', 'email',)
    list_display_links = ('id',)
    search_fields = ('id', 'nome_completo', 'cpf', 'rg', 'endereco', 'telefone_de_contato', 'email',)


admin.site.register(Cadastro, CadastroAdmin)

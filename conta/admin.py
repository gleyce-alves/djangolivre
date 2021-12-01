from django.contrib import admin
from conta.models import Conta

class ContaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cadastro', 'agencia', 'numero_conta', 'saldo')
    list_display_links = ('id',)
    search_fields = ('id', 'cadastro', 'agencia', 'numero_conta', 'saldo',)

admin.site.register(Conta, ContaAdmin)

from django.contrib import admin
from .models import *

@admin.action(description="Habilitar Registros Selecionados")
def habilitar_pessoas(ModelAdmin, request, queryset):
    for p in queryset:
        p.ativo = True
        p.save()

@admin.action(description="Desabilitar Registros Selecionados")
def desabilitar_pessoas(ModelAdmin, request, queryset):
    queryset.update(ativo=False)

class PessoaCustomizado(admin.ModelAdmin):
    list_display = ('nome', 'email', 'celular', 'funcao', 'nascimento', 'calcula_idade', 'ativo')
    actions = [habilitar_pessoas, desabilitar_pessoas]

    # Define o título da coluna "Idade" na listagem do admin
    @admin.display(description='Idade')
    # Coluna calculada: o admin chama este método para cada pessoa (obj) da lista
    def calcula_idade(self, obj):
        from datetime import date
        # Data de hoje, usada como referência para o cálculo
        hoje = date.today()
        # Sem data de nascimento cadastrada, não há como calcular a idade
        if obj.nascimento is None:
            return None
        # Idade aproximada: subtrai apenas os anos, sem considerar mês e dia
        idade = hoje.year - obj.nascimento.year
        # O valor retornado é o que aparece na coluna
        return idade

admin.site.register(pessoa, PessoaCustomizado)

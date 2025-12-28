from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'criada_em')
    list_filter = ('status',)
    search_fields = ('titulo', 'descricao')
    ordering = ('-criada_em',)
    
    def save_model(self, request, obj, form, change):
        obj.full_clean()
        return super().save_model(request, obj, form, change)
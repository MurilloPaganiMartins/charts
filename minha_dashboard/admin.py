from django.contrib import admin
from .models import Aluno, Entradas


class EntradasAdmin(admin.ModelAdmin):
    filter_horizontal = ('alunos',)
    readonly_fields = ('alunos_em_sala',)


# Register your models here.
admin.site.register(Aluno)
admin.site.register(Entradas, EntradasAdmin)


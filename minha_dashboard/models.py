from typing import ClassVar
from django.db import models
import datetime
from django.utils import timezone


class Aluno(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.nome)


class Entradas(models.Model):
    alunos = models.ManyToManyField(Aluno, related_name='entradas_alunos')
    temperatura = models.FloatField()
    lux = models.FloatField()
    humidade = models.FloatField()
    voltagem = models.FloatField()
    data = models.DateTimeField(default=timezone.now)

    @property
    def alunos_em_sala(self):
        return self.alunos.count()

    def __str__(self):
        # Adjust timezone if necessary
        delayed_time = self.data - timezone.timedelta(hours=3)
        return delayed_time.strftime('%Y-%m-%d %H:%M:%S')

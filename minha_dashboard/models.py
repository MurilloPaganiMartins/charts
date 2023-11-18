from typing import ClassVar
from django.db import models
import datetime


class Aluno(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.nome)


class Entradas(models.Model):

    alunos = models.ManyToManyField(Aluno, related_name='entradas_alunos')
    temperatura = models.FloatField()
    lux = models.FloatField()
    humidade = models.FloatField()
    data = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        delayed_time = self.data - datetime.timedelta(hours=3)
        return delayed_time.strftime('%Y-%m-%d %H:%M:%S')
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from datetime import datetime
from django.db.models import Sum
from statistics import mean
from .models import Aluno, Entradas

# Create your views here.


def home(request):
    return render(request, 'home.html')


def medias(request):
    x = Entradas.objects.all()

    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data_temperatura = []
    data_humidade = []
    data_lux = []
    labels = []
    cont = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1

        temperatures = [i.temperatura for i in x if i.data.month == mes and i.data.year == ano]
        humidities = [i.humidade for i in x if i.data.month == mes and i.data.year == ano]
        lux_values = [i.lux for i in x if i.data.month == mes and i.data.year == ano]

        total_temperature = sum(temperatures) if temperatures else 0
        total_humidade = sum(humidities) if humidities else 0
        total_lux = sum(lux_values) if lux_values else 0

        num_entries = len(temperatures)

        average_temperature = total_temperature / num_entries if num_entries > 0 else 0
        average_humidade = total_humidade / num_entries if num_entries > 0 else 0
        average_lux = total_lux / num_entries if num_entries > 0 else 0

        labels.append(meses[mes - 1])
        data_temperatura.append(average_temperature)
        data_humidade.append(average_humidade)
        data_lux.append(average_lux)

        cont += 1

    data_json = {'data_temperatura': data_temperatura[::-1], 'data_humidade': data_humidade[::-1], 'data_lux': data_lux[::-1], 'labels': labels[::-1]}

    return JsonResponse(data_json)
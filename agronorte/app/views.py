from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.

def horario (request):
    horario = datetime.datetime.now()
    return HttpResponse(horario)  
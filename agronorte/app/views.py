from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from .forms import ClienteForm

# Create your views here.

def horario (request):
    horario = datetime.datetime.now()
    return render(request, 'lista_horario.html', context={'horario':horario})


def form_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('horario')
    form = ClienteForm()
    return render(request, 'form_cliente.html', context={'form': form})
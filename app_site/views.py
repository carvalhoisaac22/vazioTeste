from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app_site/home.html')


def nutricao(request):
    return render(request, 'app_site/nutricao.html')



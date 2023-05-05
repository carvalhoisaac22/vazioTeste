from django.contrib import admin
from django.urls import include, path
from .views import horario, form_cliente


urlpatterns = [
    path('horario',horario),
    path('form_cliente', form_cliente ),
    

]
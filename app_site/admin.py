from django.contrib import admin

from app_site.models import Categoria, Transacao

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Transacao)
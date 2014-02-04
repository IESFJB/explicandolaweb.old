# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen', 'orden')
    ordering = ('orden',)

admin.site.register(Categoria, CategoriaAdmin)

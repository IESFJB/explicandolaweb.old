# -*- encoding: utf-8 -*-


from django.contrib import admin
from .models import Curso, Capitulo
from mce_filebrowser.admin import MCEFilebrowserAdmin


class CapituloAdmin(MCEFilebrowserAdmin):
    list_display = ('curso', 'titulo', 'creado', 'activo', 'destacado', )


class CursoAdmin(MCEFilebrowserAdmin):
    list_display = ('titulo', 'creado', 'activo', 'destacado', )


admin.site.register(Curso, CursoAdmin)
admin.site.register(Capitulo, CapituloAdmin)

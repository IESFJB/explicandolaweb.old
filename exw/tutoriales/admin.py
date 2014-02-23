# -*- encoding: utf-8 -*-


from django.contrib import admin
from .models import Tutorial
from mce_filebrowser.admin import MCEFilebrowserAdmin


class TutorialAdmin(MCEFilebrowserAdmin):
    list_display = ('titulo', 'autor', 'publicacion', 'creado', 'actualizado', 'activo', 'destacado', 'imagen_destacada')

admin.site.register(Tutorial, TutorialAdmin)

# -*- encoding: utf-8 -*-


from django.contrib import admin
from .models import Post
from mce_filebrowser.admin import MCEFilebrowserAdmin


class PostAdmin(MCEFilebrowserAdmin):
    list_display = ('titulo', 'publicacion', 'creado', 'actualizado', 'activo', 'destacado', 'imagen_destacada')


admin.site.register(Post, PostAdmin)

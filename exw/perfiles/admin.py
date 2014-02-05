# -*- encoding: utf-8 -*-


from django.contrib import admin
from .models import Perfil
from django.contrib.auth.models import User


class PerfilInline(admin.StackedInline):
    model = Perfil
    max_num = 1
    can_delete = False


class PerfilAdmin(admin.ModelAdmin):
    inlines = [PerfilInline]


admin.site.unregister(User)
admin.site.register(User, PerfilAdmin)

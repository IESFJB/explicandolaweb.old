# -*- coding: utf-8 -*-


from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User)
    foto = models.ImageField(upload_to='profiles/', blank=True, null=True)
    descripcion = models.TextField(max_length=500, blank=True, null=True)
    facebook = models.CharField(max_length=140, blank=True, null=True)
    twitter = models.CharField(max_length=140, blank=True, null=True)
    google = models.CharField(max_length=140, blank=True, null=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

from django.contrib.sites.models import get_current_site

from categorias.models import Categoria

from django.utils.encoding import force_unicode

class Auditoria(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Articulo(Auditoria):
    titulo = models.CharField(max_length=150)
    autor = models.ForeignKey(User)
    destacado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria)
    contenido = HTMLField(blank=True)
    extracto = HTMLField(blank=True)

    def __unicode__(self):
        return force_unicode(self.titulo)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        pass

    def get_ruta_completa(self):
        request = None
        ruta_completa = ''.join(['http://', get_current_site(request).domain, self.get_absolute_url()])
        return ruta_completa

    def get_meta_description(self):
        return self.titulo

    def get_compartir_facebook(self):
        return 'http://www.facebook.com/sharer.php?u='+self.get_ruta_completa()

    def get_compartir_twitter(self):
        return 'http://twitter.com/share?url='+self.get_ruta_completa()

    def get_compartir_google(self):
        return 'http://google.com/compartir/'+self.get_ruta_completa()


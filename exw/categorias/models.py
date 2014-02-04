# -*- encoding: utf-8 -*-

from django.db import models
#from articulos.models import Auditoria
from tinymce.models import HTMLField


class Auditoria(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Categoria(Auditoria):
    nombre = models.CharField(max_length=100)
    descripcion = HTMLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='categorias/')
    orden = models.PositiveIntegerField(max_length=2, default=1)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Categoría'
        verbose_name_plural = u'Categorías'

    #def get_absolute_url(self):
    #    return reverse('articulos.views.detalle_categoria_articulo', kwargs={'pk': self.pk, 'slug': slugify(self.nombre)})

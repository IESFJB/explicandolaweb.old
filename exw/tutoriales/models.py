# -*- encoding: utf-8 -*-


from django.db import models

from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from datetime import datetime    

from articulos.models import Articulo


class Tutorial(Articulo):
    tags = TaggableManager(blank=True)
    imagen_destacada = models.ImageField(upload_to='tutoriales/%Y/%m/%d/')
    video = models.CharField(max_length=100, blank=True, null=True)
    publicacion = models.DateTimeField("F. de Publicación", default=datetime.now)
    nivel = models.PositiveSmallIntegerField(default=0, blank=True, null=False)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = u'Tutorial'
        verbose_name_plural = u'Tutoriales'

    def get_absolute_url(self):
        return reverse('tutoriales.views.detalle_tutorial', kwargs={'pk': self.pk, 'slug': slugify(self.titulo)})

    def get_meta_description(self):
        return '%s - Explicando la Web' % self.titulo

    def get_anterior(self):
        anterior = Articulo.objects.filter(creado__lt=self.creado).order_by('creado')
        if anterior.count() > 0:
            anterior = anterior[0]
        else:
            anterior = False
        return anterior

    def get_siguiente(self):
        siguiente = Articulo.objects.filter(creado__gt=self.creado).order_by('creado')
        if siguiente.count() > 0:
            siguiente = siguiente[0]
        else:
            siguiente = False
        return siguiente



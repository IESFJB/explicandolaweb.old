# -*- encoding: utf-8 -*-


from django.db import models

from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from datetime import datetime
from django.conf import settings
from unipath import Path
import os

from tinymce.models import HTMLField
from articulos.models import Articulo


class Curso(Articulo):
    ncapitulos = models.PositiveIntegerField(max_length=2, blank=True, null=True, verbose_name=u'Número de capítulos')
    temario = HTMLField(blank=True)
    imagen_destacada = models.ImageField(upload_to='cursos/')
    publicacion = models.DateTimeField("F. de Publicación", default=datetime.now)

    class Meta:
        verbose_name = u'Curso'
        verbose_name_plural = u'Cursos'

    def get_absolute_url(self):
        return reverse('cursos.views.detalle_curso', kwargs={'pk': self.pk, 'slug': slugify(self.titulo)})

    def save(self, *args, **kwargs):
        super(Curso, self).save(*args, **kwargs)

        # Obtener extensión del archivo y la ruta
        nombre    = os.path.splitext(str(self.imagen_destacada))[0]
        extension = os.path.splitext(str(self.imagen_destacada))[1]

        solo_nombre = nombre.split('/')
        solo_nombre = solo_nombre[len(solo_nombre)-1]
        #if solo_nombre != str(self.pk):
        media_blog = settings.MEDIA_ROOT.child('cursos')
        p = Path(media_blog, solo_nombre+extension)
        p.rename(p.parent+'/'+str(self.pk)+'-'+slugify(self.titulo)+extension)
        self.imagen_destacada = 'cursos/'+str(self.pk)+'-'+slugify(self.titulo)+extension
        super(Curso, self).save(*args, **kwargs)

class Capitulo(Articulo):
    curso = models.ForeignKey('Curso', related_name='Curso')
    orden = models.PositiveIntegerField(max_length=2, default=1)
    imagen_destacada = models.ImageField(upload_to='capitulos/')

    class Meta:
        verbose_name = u'Capítulo'
        verbose_name_plural = u'Capítulos'

    def get_absolute_url(self):
        return reverse('cursos.views.detalle_capitulo',
                kwargs={'pk': self.pk,
                        'slug': slugify(self.titulo),
                        'pk_curso': self.curso.pk,
                        'slug_curso': slugify(self.curso.titulo),
                })

    def get_anterior(self):
        orden_anterior = self.orden-1
        anterior = Capitulo.objects.filter(curso=self.curso).filter(orden=orden_anterior)
        if anterior.count() > 0:
            anterior = anterior[0]
        else:
            anterior = False
        return anterior

    def get_siguiente(self):
        orden_siguiente = self.orden+1
        siguiente = Capitulo.objects.filter(curso=self.curso).filter(orden=orden_siguiente)
        if siguiente.count() > 0:
            siguiente = siguiente[0]
        else:
            siguiente = False
        return siguiente

    def save(self, *args, **kwargs):
        super(Capitulo, self).save(*args, **kwargs)

        # Obtener extensión del archivo y la ruta
        nombre    = os.path.splitext(str(self.imagen_destacada))[0]
        extension = os.path.splitext(str(self.imagen_destacada))[1]

        solo_nombre = nombre.split('/')
        solo_nombre = solo_nombre[len(solo_nombre)-1]
        #if solo_nombre != str(self.pk):
        media_blog = settings.MEDIA_ROOT.child('capitulos')
        p = Path(media_blog, solo_nombre+extension)
        p.rename(p.parent+'/'+str(self.pk)+'-'+slugify(self.titulo)+extension)
        self.imagen_destacada = 'capitulos/'+str(self.pk)+'-'+slugify(self.titulo)+extension
        super(Capitulo, self).save(*args, **kwargs)

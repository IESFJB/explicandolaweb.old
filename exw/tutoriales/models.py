# -*- encoding: utf-8 -*-


from django.db import models

from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from datetime import datetime
from django.conf import settings
from unipath import Path
import os

from articulos.models import Articulo

class Tutorial(Articulo):
    tags = TaggableManager(blank=True)
    imagen_destacada = models.ImageField(upload_to='tutoriales/')
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
        anterior = Tutorial.objects.filter(publicacion__lt=self.publicacion).order_by('publicacion')
        if anterior.count() > 0:
            anterior = anterior[0]
        else:
            anterior = False
        return anterior

    def get_siguiente(self):
        siguiente = Tutorial.objects.filter(publicacion__gt=self.publicacion).order_by('publicacion')
        if siguiente.count() > 0:
            siguiente = siguiente[0]
        else:
            siguiente = False
        return siguiente

    def save(self, *args, **kwargs):
        if self.destacado:
            for tut in Tutorial.objects.filter(destacado=True):
                tut.destacado = False
                tut.save()
        super(Tutorial, self).save(*args, **kwargs)

        # Obtener extensión del archivo y la ruta
        nombre    = os.path.splitext(str(self.imagen_destacada))[0]
        extension = os.path.splitext(str(self.imagen_destacada))[1]

        solo_nombre = nombre.split('/')
        solo_nombre = solo_nombre[len(solo_nombre)-1]
        if solo_nombre != str(self.pk):
            media_blog = settings.MEDIA_ROOT.child('tutoriales')
            p = Path(media_blog, solo_nombre+extension)
            p.rename(p.parent+'/'+str(self.pk)+extension)
            self.imagen_destacada = 'tutoriales/'+str(self.pk)+extension
            #self.save()
            #os.rename("media/"+str(self.imagen_destacada),"media/tutoriales/"+str(self.pk)+extension)
            #self.imagen_destacada = "tutoriales/"+str(self.pk)+extension
            super(Tutorial, self).save(*args, **kwargs)

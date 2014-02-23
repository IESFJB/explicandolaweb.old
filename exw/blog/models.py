# -*- encoding: utf-8 -*-


from django.db import models
from articulos.models import Articulo
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from datetime import datetime
from django.conf import settings
from unipath import Path
import os

class Post(Articulo):
    tags = TaggableManager(blank=True)
    imagen_destacada = models.ImageField(upload_to='blog/')
    publicacion = models.DateTimeField("F. de Publicación", default=datetime.now)

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog.views.detalle_post', kwargs={'pk': self.pk, 'slug': slugify(self.titulo)})

    def get_anterior(self):
        anterior = Post.objects.filter(publicacion__lt=self.publicacion).order_by('publicacion')
        if anterior.count() > 0:
            anterior = anterior[0]
        else:
            anterior = False
        return anterior

    def get_siguiente(self):
        siguiente = Post.objects.filter(publicacion__gt=self.publicacion).order_by('publicacion')
        if siguiente.count() > 0:
            siguiente = siguiente[0]
        else:
            siguiente = False
        return siguiente

    def save(self, *args, **kwargs):
        if self.destacado:
            for post in Post.objects.filter(destacado=True):
                post.destacado = False
                post.save()
        super(Post, self).save(*args, **kwargs)

        # Obtener extensión del archivo y la ruta
        nombre    = os.path.splitext(str(self.imagen_destacada))[0]
        extension = os.path.splitext(str(self.imagen_destacada))[1]

        solo_nombre = nombre.split('/')
        solo_nombre = solo_nombre[len(solo_nombre)-1]
        #if solo_nombre != str(self.pk):
        media_blog = settings.MEDIA_ROOT.child('blog')
        p = Path(media_blog, solo_nombre+extension)
        p.rename(p.parent+'/'+str(self.pk)+'-'+slugify(self.titulo)+extension)
        self.imagen_destacada = 'blog/'+str(self.pk)+'-'+slugify(self.titulo)+extension
        super(Post, self).save(*args, **kwargs)

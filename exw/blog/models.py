# -*- encoding: utf-8 -*-


from django.db import models
from articulos.models import Articulo
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from datetime import datetime
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

        # Obtener extensión del archivo
        nombre    = os.path.splitext(str(self.imagen_destacada))[0]
        extension = os.path.splitext(str(self.imagen_destacada))[1]

        trozos = nombre.split('/')
        if trozos[len(trozos)-1] != str(self.pk):
            #os.rename("media/"+str(self.imagen_destacada),"media/blog/"+str(self.pk)+extension)
            os.rename(str(self.imagen_destacada),"blog/"+str(self.pk)+extension)
            self.imagen_destacada = "blog/"+str(self.pk)+extension
            #self.imagen_destacada ="media/"+str(self.imagen_destacada)
            super(Post, self).save(*args, **kwargs)

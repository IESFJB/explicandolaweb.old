# -*- encoding: utf-8 -*-


from django.db import models
from articulos.models import Articulo
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from datetime import datetime    


class Post(Articulo):
    tags = TaggableManager(blank=True)
    fb_imagen = models.ImageField(upload_to='blog/facebook/%Y/%m/%d/', blank=True, null=True)
    imagen_destacada = models.ImageField(upload_to='blog/%Y/%m/%d/')
    publicacion = models.DateTimeField("F. de Publicación", default=datetime.now)

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog.views.detalle_post', kwargs={'pk': self.pk, 'slug': slugify(self.titulo)})

    def save(self, *args, **kwargs):
        if self.destacado:
            for post in Post.objects.filter(destacado=True):
                post.destacado = False
                post.save()
        super(Post, self).save(*args, **kwargs)
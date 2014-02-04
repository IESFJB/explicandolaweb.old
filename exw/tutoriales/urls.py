# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url
from categorias.views import detalle_categoria_tutorial

urlpatterns = patterns('tutoriales.views',
    url(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/$',             'detalle_tutorial',             name='detalle_tutorial'),
    url(r'^archivo/(?P<pk>\d+)-(?P<slug>[\w-]+)/$',     detalle_categoria_tutorial,     name='detalle_categoria_tutorial'),
)

# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('cursos.views',
    url(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/$',                                             'detalle_curso',                name='detalle_curso'),
    url(r'^(?P<pk_curso>\d+)-(?P<slug_curso>[\w-]+)/(?P<pk>\d+)-(?P<slug>[\w-]+)/$',    'detalle_capitulo',             name='detalle_capitulo'),
)

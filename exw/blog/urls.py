# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, url


urlpatterns = patterns('blog.views',
    url(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/$',             'detalle_post',            name='detalle_post'),
)

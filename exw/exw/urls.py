# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, include, url
from django.conf import settings


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^$',          'web.views.previa',         name='previa'),

    url(r'^home/$',     'web.views.home',           name='home'),

    url(r'^error/$',    'web.views.error_template', name='error_template'),

    url(r'^tutoriales/$', 'web.views.tutoriales',   name='tutoriales'),

    url(r'^tutoriales/', include('tutoriales.urls')),

    url(r'^cursos/$',   'web.views.cursos',         name='cursos'),

    url(r'^cursos/',    include('cursos.urls')),

    url(r'^blog/$',     'web.views.blog',           name='blog'),

    url(r'^blog/',      include('blog.urls')), 

    url(r'^contacto/$', 'web.views.contacto',       name='contacto'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}),

    (r'^tinymce/',          include('tinymce.urls')),
    (r'^mce_filebrowser/',  include('mce_filebrowser.urls')),
    url(r'^admin_tools/',   include('admin_tools.urls')),
    url(r'^admin/', include('admin_honeypot.urls')),
    url(r'^exw_panel/',     include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT})
    )
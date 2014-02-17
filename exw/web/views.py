# -*- encoding: utf-8 -*-


from django.views.generic import TemplateView
from tutoriales.models import Tutorial
from cursos.models import Curso
from blog.models import Post

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def class_view_decorator(function_decorator):
    def simple_decorator(View):
        View.dispatch = method_decorator(function_decorator)(View.dispatch)
        return View

    return simple_decorator


@class_view_decorator(login_required)
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['articulos'] = Tutorial.objects.filter(destacado=False)[:9]
        destacado = Tutorial.objects.filter(destacado=True)
        if destacado.count() > 0:
            context['destacado'] = destacado[0]
        return context

home = Home.as_view()

@class_view_decorator(login_required)
class Tutoriales(TemplateView):
    template_name = "tutoriales.html"

    def get_context_data(self, **kwargs):
        context = super(Tutoriales, self).get_context_data(**kwargs)
        context['articulos'] = Tutorial.objects.filter(activo=True)[:9]
        context['destacado'] = Tutorial.objects.get(destacado=True)
        return context

tutoriales = Tutoriales.as_view()

@class_view_decorator(login_required)
class Cursos(TemplateView):
    template_name = "cursos/curso_list.html"

    def get_context_data(self, **kwargs):
        context = super(Cursos, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.filter(activo=True)[:9]
        destacado = Curso.objects.filter(destacado=True)
        if destacado.count() > 0:
            context['destacado'] = destacado[0]
        return context

cursos = Cursos.as_view()

@class_view_decorator(login_required)
class Blog(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super(Blog, self).get_context_data(**kwargs)
        context['articulos'] = Post.objects.filter(destacado=False)[:9]
        destacado = Post.objects.filter(destacado=True)
        if destacado.count() > 0:
            context['destacado'] = destacado[0]
        return context

blog = Blog.as_view()

@class_view_decorator(login_required)
class Contacto(TemplateView):
    template_name = "home.html"

contacto = Contacto.as_view()

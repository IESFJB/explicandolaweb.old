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


class ErrorTemplate(TemplateView):
    template_name = "404.html"

error_template = ErrorTemplate.as_view()


class Previa(TemplateView):
    template_name = "previa.html"

previa = Previa.as_view()


#@class_view_decorator(login_required)
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['tutoriales'] = Tutorial.objects.all().filter(destacado=False).order_by('-publicacion')[:6]
        context['posts'] = Post.objects.all().filter(destacado=False).order_by('-publicacion')[:6]
        
        #Buscamos el tutorial y el post destacado más nuevo
        t_destacado = Tutorial.objects.filter(destacado=True).order_by('-publicacion')
        p_destacado = Post.objects.filter(destacado=True).order_by('-publicacion')

        if t_destacado.count() > 0:
            t_destacado = t_destacado[0]
            #Buscamos el post destacado más nuevo
            if p_destacado.count() > 0:
                p_destacado = p_destacado[0]
                #Nos quedamos con el más nuevo
                print t_destacado.publicacion
                print p_destacado.publicacion
                if t_destacado.publicacion < p_destacado.publicacion:
                    context['destacado'] = p_destacado
                else:
                    context['destacado'] = t_destacado                
            #Si no hay el destacado será el tutorial
            else:
                context['destacado'] = t_destacado
        else:
            #Buscamos el post destacado más nuevo
            if p_destacado.count() > 0:
                context['destacado'] = p_destacado
        return context

home = Home.as_view()


#@class_view_decorator(login_required)
class Tutoriales(TemplateView):
    template_name = "tutoriales.html"

    def get_context_data(self, **kwargs):
        context = super(Tutoriales, self).get_context_data(**kwargs)
        context['articulos'] = Tutorial.objects.filter(activo=True, destacado=False)[:9]
        destacado = Tutorial.objects.filter(activo=True, destacado=True)
        if destacado.count() > 0:
            context['destacado'] = destacado[0]
        return context

tutoriales = Tutoriales.as_view()


#@class_view_decorator(login_required)
class Cursos(TemplateView):
    template_name = "cursos/curso_list.html"

    def get_context_data(self, **kwargs):
        context = super(Cursos, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.filter(activo=True, destacado=False)[:9]
        destacado = Curso.objects.filter(destacado=True)
        if destacado.count() > 0:
            context['destacado'] = destacado[0]
        return context

cursos = Cursos.as_view()


#@class_view_decorator(login_required)
class Blog(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super(Blog, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(destacado=False)[:9]
        destacado = Post.objects.filter(destacado=True)
        if destacado.count() > 0:
            context['destacado'] = destacado[0]
        return context

blog = Blog.as_view()


#@class_view_decorator(login_required)
class Exw(TemplateView):
    template_name = "exw.html"

exw = Exw.as_view()

# -*- encoding: utf-8 -*-


from django.views.generic import DetailView
from .models import Categoria
from django.shortcuts import get_object_or_404
from tutoriales.models import Tutorial
from cursos.models import Curso
from django.views.generic import TemplateView


class DetalleCategoria(TemplateView):
    template_name = "404.html"


class DetalleCategoriaTutorial(DetailView):
    model = Categoria

    def get_context_data(self, **kwargs):
        context = super(DetalleCategoriaTutorial, self).get_context_data(**kwargs)
        categoria = get_object_or_404(Categoria, pk=self.kwargs.get('pk', None))
        context['articulos'] = Tutorial.objects.filter(categoria=categoria)
        return context

detalle_categoria_tutorial = DetalleCategoriaTutorial.as_view()


class DetalleCategoriaCurso(DetailView):
    model = Categoria

    def get_context_data(self, **kwargs):
        context = super(DetalleCategoriaCurso, self).get_context_data(**kwargs)
        categoria = get_object_or_404(Categoria, pk=self.kwargs.get('pk', None))
        context['articulos'] = Curso.objects.filter(categoria=categoria)
        return context

detalle_categoria_curso = DetalleCategoriaCurso.as_view()

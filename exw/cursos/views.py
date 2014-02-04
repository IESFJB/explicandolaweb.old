from django.views.generic import DetailView, ListView
from .models import Curso, Capitulo

from django.template.defaultfilters import slugify


class DetalleCurso(DetailView):
    model = Curso

    def get_context_data(self, **kwargs):
        context = super(DetalleCurso, self).get_context_data(**kwargs)
        context['capitulos'] = Capitulo.objects.all()
        return context

detalle_curso = DetalleCurso.as_view()


class ListaCurso(ListView):
    model = Curso

lista_curso = ListaCurso.as_view()


class DetalleCapitulo(DetailView):
    model = Capitulo

    def get_context_data(self, **kwargs):
        context = super(DetalleCapitulo, self).get_context_data(**kwargs)
        curso = self.get_object()
        context['pk_curso'] = curso.pk
        context['slug_curso'] = slugify(curso.titulo)
        return context
detalle_capitulo = DetalleCapitulo.as_view()

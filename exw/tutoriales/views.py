# -*- encoding: utf-8 -*-


from django.views.generic import DetailView, ListView
from .models import Tutorial


class DetalleTutorial(DetailView):
    model = Tutorial
    context_object_name = 'articulo'

detalle_tutorial = DetalleTutorial.as_view()


class ListaTutorial(ListView):
    model = Tutorial
    context_object_name = 'articulos'

    # def get_context_data(self, **kwargs):
    #     context = super(ListaTutorial, self).get_context_data(**kwargs)
    #     context['rango'] = range(1, 4)
    #     return context

    # def get_queryset(self):
    #     return super(ListaTutorial, self).get_queryset().all()[:1]

lista_tutorial = ListaTutorial.as_view()

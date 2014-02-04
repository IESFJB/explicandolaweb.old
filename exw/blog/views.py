from django.views.generic import DetailView, ListView
from .models import Post


class DetallePost(DetailView):
    model = Post

detalle_post = DetallePost.as_view()


class ListaPost(ListView):
    model = Post

lista_post = ListaPost.as_view()

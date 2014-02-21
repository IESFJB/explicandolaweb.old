# -*- encoding: utf-8 -*-


from django.core.urlresolvers import reverse
from tutoriales.models import Tutorial
from categorias.models import Categoria
from blog.models import Post


def menu(request):
    menu = {'menu': [
        {'text': 'Tutoriales', 	 'url': reverse('tutoriales')},
        {'text': 'Cursos', 		 'url': reverse('cursos')},
        {'text': 'Blog', 		 'url': reverse('blog')},
        {'text': 'Exw', 	     'url': reverse('exw')},
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
            break
        else:
            if item['text'].replace('/', '').lower() in request.get_full_path():
                item['active'] = True
                break
    return menu


def categorias_tutoriales(request):
    cat_contutoriales = Tutorial.objects.values_list('categoria', flat=True).distinct()
    categorias_tutoriales = Categoria.objects.filter(pk__in=cat_contutoriales).order_by('orden')
    categorias_tutoriales = {
        'categorias_tutoriales': categorias_tutoriales,
    }
    return categorias_tutoriales

def ultimos_tutoriales(request):
    ultimos_tutoriales = Tutorial.objects.all()
    ultimos_tutoriales = {
        'ultimos_tutoriales': ultimos_tutoriales,
    }
    return ultimos_tutoriales

def ultimos_capitulos(request):
    ultimos_capitulos = Tutorial.objects.all()
    ultimos_capitulos = {
        'ultimos_capitulos': ultimos_capitulos,
    }
    return ultimos_capitulos

def ultimos_post(request):
    ultimos_posts = Post.objects.all()
    ultimos_posts = {
        'ultimos_posts': ultimos_posts,
    }
    return ultimos_posts

# -*- encoding: utf-8 -*-


from django.test import TestCase
from django.contrib.auth.models import User

from articulos.models import Articulo
from categorias.models import Categoria
from cursos.models import Curso, Capitulo
from blog.models import Post


class ExwTest(TestCase):

    def setUp(self):

        #Usuario
        self.usuario = User.objects.create_user('test', 'test@test.com', 'password')
        self.assertEqual(1, User.objects.count())

        #Categoría
        self.categoria = Categoria()
        self.categoria.nombre = 'Categoria de prueba'
        self.categoria.descripcion = 'Descripcion de prueba'
        self.categoria.imagen = ''
        self.categoria.orden = 1
        self.categoria.save()

        #Articulo
        self.articulo = Articulo()
        self.articulo.titulo = "Hola k ase"
        self.articulo.categoria = self.categoria
        self.articulo.autor = self.usuario
        self.articulo.contenido = ''
        self.articulo.extracto = ''
        self.articulo.imagen_destacada = ''
        self.articulo.destacado = True
        self.articulo.save()

        #Curso
        self.curso = Curso()
        self.curso.titulo = "Hola k ase"
        self.curso.categoria = self.categoria
        self.curso.autor = self.usuario
        self.curso.contenido = ''
        self.curso.extracto = ''
        self.curso.imagen_destacada = ''
        self.curso.destacado = True
        self.curso.save()

        #Capítulo
        self.capitulo = Capitulo()
        self.capitulo.titulo = "Hola k ase"
        self.capitulo.categoria = self.categoria
        self.capitulo.curso = self.curso
        self.capitulo.autor = self.usuario
        self.capitulo.contenido = ''
        self.capitulo.extracto = ''
        self.capitulo.imagen_destacada = ''
        self.capitulo.destacado = True
        self.capitulo.orden = 1
        self.capitulo.save()

        #Post
        self.post = Post()
        self.post.titulo = "Hola k ase"
        self.post.categoria = self.categoria
        self.post.autor = self.usuario
        self.post.contenido = ''
        self.post.extracto = ''
        self.post.imagen_destacada = ''
        self.post.destacado = True
        self.post.save()

    def test_fields(self):

        #Usuario
        usuario = User.objects.get(pk=1)
        self.assertEqual(usuario, self.usuario)
        self.assertEqual(usuario.id, self.usuario.id)
        self.assertEqual(usuario.first_name, self.usuario.first_name)
        self.assertEqual(usuario.last_name, self.usuario.last_name)

        #Categoría
        cat = Categoria.objects.get(pk=1)
        self.assertEqual(cat.nombre, 'Categoria de prueba')
        self.assertEqual(cat.descripcion, 'Descripcion de prueba')
        self.assertEqual(cat.imagen, '')
        self.assertEqual(cat.orden, 1)

        #Articulo
        art = Articulo.objects.get(pk=self.articulo.id)
        self.assertEqual("Hola k ase", art.titulo)
        self.assertEqual(cat, art.categoria)
        self.assertEqual(usuario, art.autor)
        self.assertEqual('', art.contenido)
        self.assertEqual('', art.extracto)
        self.assertEqual('', art.imagen_destacada)
        self.assertEqual(True, art.destacado)

        #Curso
        curso = Curso.objects.get(pk=self.curso.id)
        self.assertEqual("Hola k ase", curso.titulo)
        self.assertEqual(cat, curso.categoria)
        self.assertEqual(usuario, curso.autor)
        self.assertEqual('', curso.contenido)
        self.assertEqual('', curso.extracto)
        self.assertEqual('', curso.imagen_destacada)
        self.assertEqual(True, curso.destacado)

        #Capítulo
        capitulo = Capitulo.objects.get(pk=self.capitulo.id)
        self.assertEqual("Hola k ase", capitulo.titulo)
        self.assertEqual(cat, capitulo.categoria)
        self.assertEqual(curso, capitulo.curso)
        self.assertEqual(usuario, capitulo.autor)
        self.assertEqual('', capitulo.contenido)
        self.assertEqual('', capitulo.extracto)
        self.assertEqual('', capitulo.imagen_destacada)
        self.assertEqual(True, capitulo.destacado)

        #Post
        post = Post.objects.get(pk=1)
        self.assertEqual("Hola k ase", post.titulo)
        self.assertEqual(cat, post.categoria)
        self.assertEqual(usuario, post.autor)
        self.assertEqual('', post.contenido)
        self.assertEqual('', post.extracto)
        self.assertEqual('', post.imagen_destacada)
        self.assertEqual(True, post.destacado)

    def test_urls(self):

        #Home
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

        #Tutoriales
        response = self.client.get('/tutoriales/')
        self.assertEqual(200, response.status_code)

        #Vista detalle del tutorial
        response = self.client.get(self.articulo.get_absolute_url())
        self.assertEqual(200, response.status_code)

        #Cursos
        response = self.client.get('/cursos/')
        self.assertEqual(200, response.status_code)

        #Detalle de Curso
        response = self.client.get(self.curso.get_absolute_url())
        self.assertEqual(200, response.status_code)

        #Detalle de Capítulo
        response = self.client.get(self.capitulo.get_absolute_url())
        self.assertEqual(200, response.status_code)

        #Blog
        response = self.client.get('/blog/')
        self.assertEqual(200, response.status_code)

        #Detalle de Post
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(200, response.status_code)

        # #Contacto
        # response = self.client.get('/contacto/')
        # self.assertEqual(200, response.status_code)

        #404
        response = self.client.get('/hola-que-ase/')
        self.assertEqual(404, response.status_code)

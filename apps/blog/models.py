from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(verbose_name = "Nombre de la categoria", max_length = 100)
    status = models.BooleanField(verbose_name = "Estatus", default = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombres = models.CharField(verbose_name = "Nombres del autor", max_length = 255)
    apellidos = models.CharField(verbose_name = "Apellidos", max_length = 255)
    facebook = models.URLField(verbose_name = "Facebook", null = True, blank = True)
    twitter = models.URLField(verbose_name = "Twitter", null = True, blank = True)
    instagram = models.URLField(verbose_name = "Instagram", null = True, blank = True)
    web = models.URLField(verbose_name = "Web", null = True, blank = True)
    correo = models.EmailField(verbose_name = "Correo", max_length = 254)
    status = models.BooleanField(verbose_name = "Autor activo", default = True)
    created = models.DateTimeField(verbose_name = "Fecha de creacion", auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)

class Post(models.Model):
    titulo = models.CharField(verbose_name = "Titulo", max_length=200)
    slug = models.CharField(verbose_name = "Slug", max_length = 100)
    descripcion = models.CharField(verbose_name = "Descripcion", max_length=200)
    contenido = RichTextField(verbose_name="Contenido")
    imagen = models.URLField(max_length = 200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name = "Publicado/No publicado", default = True)
    created = models.DateTimeField(verbose_name = "Fecha de creacion", auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
    
    
from django.db import models

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
    
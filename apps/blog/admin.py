from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'status', 'created')

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos']
    list_display = ('nombres', 'apellidos', 'correo', 'created')


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
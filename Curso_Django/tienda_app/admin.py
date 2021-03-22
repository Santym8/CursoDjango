from django.contrib import admin
from .models import Producto, CategoriaProductos


# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

class CategoriaProductosAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

admin.site.register(CategoriaProductos, CategoriaProductosAdmin)
admin.site.register(Producto, ProductoAdmin)
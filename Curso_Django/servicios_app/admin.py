from django.contrib import admin
from servicios_app.models import Servicio

# Register your models here.

class ServicoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Servicio, ServicoAdmin)
from django.contrib import admin
from .models import Contacto
from .models import Producto

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre","apellido","correo","tipo_consulta","mensajes"]
    search_fields = ["nombre","apellido"]
    list_filter = ["tipo_consulta"]
    list_per_page = 5



admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Producto)
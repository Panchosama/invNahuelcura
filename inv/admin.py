from django.contrib import admin
from .models import Clase, Tipo, Objeto, Ubicacion, Articulo, Asignacion, Edificio, Piso, Sala
# Register your models here.

#admin.site.register(Tipo)
admin.site.register(Objeto)
admin.site.register(Ubicacion)
admin.site.register(Articulo)
#admin.site.register(Asignacion)
admin.site.register(Edificio)
admin.site.register(Piso)
#admin.site.register(Sala)

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
		list_display = ('nombre','codigo')
		list_filter = ('nombre','codigo')
		ordering = ('nombre',)
		search_field =('nombre',)
		
@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
		list_display = ('nombre','clase')
		list_filter = ('clase',)
		ordering = ('nombre',)
		search_field =('nombre',)
		
@admin.register(Sala)
class TipoAdmin(admin.ModelAdmin):
		list_display = ('piso','nombre','uso')
		list_filter = ('piso','uso',)
		ordering = ('piso',)
		search_field =('piso',)

@admin.register(Asignacion)
class ClaseAdmin(admin.ModelAdmin):
		list_display = ('objeto','sala','edificio','cantidad')
		list_filter = ('objeto','sala')
		ordering = ('edificio','sala',)
		search_field =('objeto','sala',)

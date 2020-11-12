from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey
from  django.contrib.auth.models import User

#Clases definiendo los objetos inventariados
class Clase(models.Model):
	nombre=models.CharField(max_length=50)
	codigo=models.CharField(max_length=3, null=True, blank=True)
	descripcion=models.TextField(default="")
	
	def __str__(self):
		return self.codigo
	
	def cod(self):
		return self.codigo
		
class Tipo(models.Model):
	clase=models.ForeignKey(Clase, on_delete=models.CASCADE)
	nombre=models.CharField(max_length=50)
	
	def __str__(self):
		return self.nombre

class Objeto(models.Model):
	tipo=models.ForeignKey(Tipo, on_delete=models.CASCADE)
	nombre=models.CharField(max_length=100)

	def __str__(self):
		return self.nombre
		
class Articulo(models.Model):
	objeto=models.ForeignKey(Objeto, on_delete=models.CASCADE)
	codigo=models.CharField(max_length=7)
	nombre=models.TextField(default="")
	estado=models.CharField(max_length=1)
	fecha=models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.nombre
	
#-------------------------------------------------
#Clase de ubicaciones
class Edificio(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.TextField(default="")
	
	def __str__(self):
		return self.nombre
		
class Piso(models.Model):
	edificio=models.ForeignKey(Edificio, on_delete=models.PROTECT)
	nombre=models.CharField(max_length=50)
	
	def __str__(self):
		return "%s - %s"%(self.edificio.nombre,self.nombre)

class Sala(models.Model):
	piso=models.ForeignKey(Piso, on_delete=models.PROTECT)
	nombre=models.CharField(max_length=50)
	uso=models.CharField(max_length=100)
	descripcion=models.TextField(default="")
	
	def __str__(self):
		return "%s - %s"%(self.uso,self.nombre)
	
class Ubicacion(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=150)
	  
	class Meta:
		verbose_name_plural="Ubicaciones"
	
	def __str__(self):
		return self.nombre


class Asignacion(models.Model):
	edificio=models.ForeignKey(Edificio, on_delete=models.PROTECT, null=True)
	piso=ChainedForeignKey(
		Piso,
		chained_field='edificio',
		chained_model_field='edificio',
		show_all=False,
		auto_choose=True,
		sort=True,
		null=True)
	sala=ChainedForeignKey(
		Sala,
		chained_field='piso',
		chained_model_field='piso',
		show_all=False,
		auto_choose=True,
		sort=True,
		null=True)
	tipo=models.ForeignKey(Tipo, on_delete=models.PROTECT, null=True)
	objeto=ChainedForeignKey(
		Objeto,
		chained_field='tipo',
		chained_model_field='tipo',
		show_all=False,
		auto_choose=True,
		sort=True,
		null=True)
	cantidad=models.PositiveSmallIntegerField(default=0)
	observaciones=models.TextField(default="", blank=True)
	fecha=models.DateTimeField(default=timezone.now)
	usuario=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	
	class Meta:
		verbose_name_plural="Asignaciones"
		
	def guardar(self):
		self.fecha=timezone.now()
		self.save()


	def __str__(self):
		return '%s - %s - %i'%(self.sala, self.objeto, self.cantidad)
	

class Movimiento(models.Model):
	tipo=models.ForeignKey(Tipo, on_delete=models.PROTECT, null=True)
	objeto=models.ForeignKey(Objeto, on_delete=models.PROTECT, null=True)
	cantidad=models.PositiveSmallIntegerField(default=0)
	origen=models.ForeignKey(Sala, related_name='origen', on_delete=models.PROTECT, null=True)
	destino=models.ForeignKey(Sala, related_name='destino', on_delete=models.PROTECT, null=True)
	usuario=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	fecha=models.DateTimeField(default=timezone.now)

	def guardar(self):
		self.fecha=timezone.now()
		self.save()




	
#class Movimiento(models.Model):
#	objeto=Models.ForeignKey(Objeto, on_delete=models.PROTECT, null=True)


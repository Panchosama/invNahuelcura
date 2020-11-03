from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Asignacion, Edificio, Piso, Sala, Tipo, Objeto
from .forms import AsignacionForm
from django.views.generic import TemplateView, CreateView
from django.db.models import Sum

def index(request):
	return render(request, 'index.html')
	

class AsignacionNew(CreateView):
	template_name='asignacion_edit.html'
	model=Asignacion
	fields= ['edificio','piso','sala','tipo','objeto','cantidad','observaciones']
	success_url="/inventario/asignar"

	def get_context_data(self, **kwargs):
		context = super(AsignacionNew, self).get_context_data(**kwargs)
		context['edificios']= Edificio.objects.all()
		context['pisos']=Piso.objects.all()
		context['salas']=Sala.objects.all()
		context['tipos']=Tipo.objects.all().order_by('nombre')
		context['objetos']=Objeto.objects.all()
		return context


def asignacion_list(request):
	asignaciones= Asignacion.objects.all().order_by('sala')
	return render(request, 'asignacion_list.html', {'asignaciones':asignaciones})


def inventario(request):
	inventario = Asignacion.objects.values('objeto__nombre').annotate(cantidad=Sum('cantidad'))
	return render(request, 'inventario.html', {'inventario':inventario})

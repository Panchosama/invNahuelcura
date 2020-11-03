from django import forms

from .models import Asignacion

class AsignacionForm(forms.ModelForm):
	
	class Meta:
		model=Asignacion
		fields=('edificio','piso','sala','tipo','objeto','cantidad','observaciones')
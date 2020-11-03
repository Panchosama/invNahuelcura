"""inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
Function views

"""
from django.urls import path, include, re_path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
#	path('inventario/asignar', views.asignacion_new, name='asignacion_new'),
	path('inventario/asignar', views.AsignacionNew.as_view(), name='asignacion_new'),
	path('inventario/asignar/list', views.asignacion_list, name='asignacion_list'),
	path('inventario/listado', views.inventario, name='inventario'),
	re_path(r'^inventario/objeto/(?P<pk>[0-9]+)/$', views.objeto_detail, name='objeto_detail'),
	path('chaining/', include("smart_selects.urls")),
]

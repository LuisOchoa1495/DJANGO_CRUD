from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .forms import EmpleadoForm
from django.urls import reverse_lazy
# Create your views here.
from .models import Empleado

class InicioView(TemplateView):
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = "personas/list_all.html"
    paginate_by = 4
    ordering='first_name'
    context_object_name='empleados'
    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword",'')
        #icontains= busca buscar valores en cadena
        lista=Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = "personas/lista_empleados.html"
    paginate_by = 10
    ordering='first_name'
    context_object_name='empleados'
    model = Empleado

class ListByAreaEmpleado(ListView):
    """ListByAreaEmple"""
    template_name = "personas/list_by_area.html"
    context_object_name='empleados'
    def get_queryset(self):
        area=self.kwargs['shortname']
        lista=Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista
class ListEmpleadoByKword(ListView):
    """ListByPalabraCLave"""
    template_name = "personas/list_by_kword.html"
    context_object_name = "empleados"
    def get_queryset(self):
        print ("*************")
        palabra_clave=self.request.GET.get("kword",'')
        print("*************",palabra_clave)
        lista=Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista
    
class ListHabilidadesEmpleado(ListView):
    template_name = "personas/habilidades.html" 
    context_object_name="habilidades"

    def get_queryset(self):
        empleado=Empleado.objects.get(id=1)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "personas/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context=super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "personas/success.html"

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "personas/add.html"
    form_class=EmpleadoForm

    
    success_url= reverse_lazy('personas_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name=empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "personas/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]       
    success_url= reverse_lazy('personas_app:empleados_admin')
    
    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "personas/delete.html"
    success_url= reverse_lazy('personas_app:empleados_admin')
   
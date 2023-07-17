from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.personas.models import Empleado
from .models import Departamento
from django.views.generic import ListView
# Create your views here.
# vista que no este reform


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamentos/lista.html"
    context_object_name= 'departamentos'

class NewDepartamentoView(FormView):
    template_name='departamentos/new_departamento.html'
    form_class=NewDepartamentoForm
    success_url='/'

    def form_valid(self, form):
        print("******form_vali")

        depa=Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name']
        )
        depa.save()

        nombre=form.cleaned_data['nombre']
        apellidos=form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellidos,
            job="1",
            departamento=depa 
        )
        return super(NewDepartamentoView,self).form_valid(form)
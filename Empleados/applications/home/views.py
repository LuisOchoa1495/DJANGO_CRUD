from django.shortcuts import render
from django.views.generic import CreateView,TemplateView, ListView
from .models import prueba
from .forms import PruebaForm
# Create your views here.

class IndexView(TemplateView):
    template_name='home/home.html'

class ModeloPruebaView(ListView):
    model= prueba
    template_name='home/prueba.html'
    context_object_name='lista_prueba'

class ResumenFoundationView(ListView):
    model= prueba
    template_name='home/resumen_foundation.html'
    context_object_name='lista_prueba'

class ListView(ListView):
    template_name='home/lista.html'
    queryset = ['A','B','C']
    context_object_name='lista_prueba'

class PruebaCreateView(CreateView):
    template_name='home/add.html'
    model= prueba
    form_class= PruebaForm
    success_url='/'
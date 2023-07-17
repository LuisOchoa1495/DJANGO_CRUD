from django.contrib import admin
from django.urls import path
from . import views

app_name = 'departamentos_app'
urlpatterns = [
   path('new_departamento/', views.NewDepartamentoView.as_view(),name='nuevo_departamento'),  
   path(
      'departamento-lista/',
      views.DepartamentoListView.as_view(),
      name='departamento_list'),  

]
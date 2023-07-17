from django.urls import path
from . import views
urlpatterns = [
    path('prueba/', views.IndexView.as_view()),
    path('lista/', views.ListView.as_view()),
    path('lista-prueba/', views.ModeloPruebaView.as_view()),
    path('add/', views.PruebaCreateView.as_view(),name='prueba_add'),
    path('resumen-foundation/', views.ResumenFoundationView.as_view(),name='prueba_add'),
]
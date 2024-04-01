from django.urls import path
from . import views

app_name = 'respuestas_abiertas'  # Esto es para namespacing de las URLs

urlpatterns = [
    path('', views.lista_cuestionarios, name='lista_cuestionarios'),
    path('cuestionario/<int:pk>/', views.cuestionario_detalle, name='cuestionario_detalle'),
]

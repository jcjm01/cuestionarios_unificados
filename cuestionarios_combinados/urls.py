from django.urls import path
from . import views

app_name = 'cuestionarios_combinados'

urlpatterns = [
    path('', views.lista_cuestionarios, name='lista_cuestionarios'),
    path('cuestionario/<int:cuestionario_id>/', views.detalle_cuestionario, name='detalle_cuestionario'),
    path('procesar_respuestas/<int:cuestionario_id>/', views.procesar_respuestas, name='procesar_respuestas'),
]

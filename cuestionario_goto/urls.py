from django.urls import path
from .views import cuestionario_completo_view, detalle_pregunta_view

app_name = 'cuestionario_goto'

urlpatterns = [
    path('cuestionario_completo/', cuestionario_completo_view, name='cuestionario_completo'),
    path('detalle_pregunta/<int:pregunta_id>/', detalle_pregunta_view, name='detalle_pregunta'),
]

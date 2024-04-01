from django.urls import path
from . import views

urlpatterns = [
    path('pregunta/<int:pregunta_id>/', views.mostrar_pregunta, name='mostrar_pregunta'),
    path('responder/<int:pregunta_id>/', views.responder_pregunta, name='responder_pregunta'),
]

# cuestionario_goto/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cuestionario/', views.cuestionario_view, name='cuestionario_view'),
]

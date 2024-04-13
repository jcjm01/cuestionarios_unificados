from django.urls import path
from .views import vista_integrada

urlpatterns = [
    path('', vista_integrada, name='vista-integrada'),
]

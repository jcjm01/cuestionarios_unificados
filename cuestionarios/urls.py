"""cuestionarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuestionario_goto/', include('cuestionario_goto.urls')),  # Incluye las URLs de la app cuestionario_goto
    path('respuestas_abiertas/', include('respuestas_abiertas.urls', namespace='respuestas_abiertas')),  # Incluye las URLs de la app respuestas_abiertas con namespace
    path('cuestionarios_combinados/', include('cuestionarios_combinados.urls', namespace='cuestionarios_combinados')),  # Incluye las URLs de la app cuestionarios_combinados con un namespace
    path('', include('cuestionarios_presentacion.urls')),  # Página de inicio/presentación
    path('vista-integrada/', include('integradora.urls')),  # Ruta única para ver integradas las apps bajo la app integradora
]

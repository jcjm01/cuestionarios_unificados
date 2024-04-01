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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuestionario_goto/', include('cuestionario_goto.urls')),  # Incluye las URLs de la app
    path('respuestas_abiertas/', include('respuestas_abiertas.urls')),
    path('cuestionarios_combinados/', include('cuestionarios_combinados.urls', namespace='cuestionarios_combinados')),
    path('', include('cuestionarios_presentacion.urls')),
]

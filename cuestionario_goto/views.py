from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Pregunta, Respuesta

def cuestionario_view(request):
    if request.method == "POST":
        # Aquí procesarías las respuestas del usuario
        respuestas_usuario = {key: value for key, value in request.POST.items() if key.startswith('respuesta_')}
        resultado = evaluar_cuestionario(respuestas_usuario)
        # Podrías redirigir a una nueva URL con el resultado o simplemente renderizarlo directamente
        return render(request, 'cuestionario_goto/resultado.html', {'resultado': resultado})
    else:
        preguntas = Pregunta.objects.all()
        return render(request, 'cuestionario_goto/cuestionario.html', {'preguntas': preguntas})

def evaluar_cuestionario(respuestas_usuario):
    puntaje_total = 0
    for pregunta_id, respuesta_id in respuestas_usuario.items():
        respuesta_id = int(respuesta_id)  # Asegúrate de convertir la ID de respuesta a int
        respuesta = Respuesta.objects.get(id=respuesta_id)
        puntaje_total += respuesta.valor
    resultado = "Un centro de contacto omnicanal sin fisuras para optimizar tanto el rendimiento de los equipos como las experiencias de los clientes" if puntaje_total >= 9 else "Un sistema de telefonía en la nube galardonado, fácil de usar y de gestionar, con voz segura, reuniones con vídeo y chat"
    return resultado

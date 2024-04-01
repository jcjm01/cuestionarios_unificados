from django.shortcuts import render, redirect
from .models import Pregunta, Respuesta

def mostrar_pregunta(request, pregunta_id):
    pregunta = Pregunta.objects.get(pk=pregunta_id)
    respuestas = Respuesta.objects.filter(pregunta=pregunta)
    return render(request, 'cuestionarios_presentacion/pregunta.html', {'pregunta': pregunta, 'respuestas': respuestas})

def responder_pregunta(request, pregunta_id):
    if request.method == 'POST':
        pregunta = Pregunta.objects.get(pk=pregunta_id)
        respuesta_id = request.POST.get('respuesta_id')
        respuesta = Respuesta.objects.get(pk=respuesta_id)

        # Lógica para determinar la siguiente pregunta basada en la respuesta seleccionada
        if respuesta.siguiente_pregunta:
            siguiente_pregunta_id = respuesta.siguiente_pregunta.id
            return redirect('mostrar_pregunta', pregunta_id=siguiente_pregunta_id)
        else:
            return render(request, 'cuestionarios_presentacion/final.html')

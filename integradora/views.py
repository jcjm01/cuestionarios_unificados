from django.shortcuts import render
from respuestas_abiertas.models import CuestionarioAbierto
from cuestionarios_combinados.models import Cuestionario
from cuestionario_goto.models import Pregunta as PreguntaGoto 

def vista_integrada(request):
    # Recuperar todos los cuestionarios de las aplicaciones respuestas_abiertas y cuestionarios_combinados
    cuestionarios_abiertos = CuestionarioAbierto.objects.all()
    preguntas_goto = PreguntaGoto.objects.all()
    cuestionarios_combinados = Cuestionario.objects.all()
    
    # Preparar el contexto con los cuestionarios recuperados
    context = {
        'cuestionarios_abiertos': cuestionarios_abiertos,
        'preguntas_goto': preguntas_goto, 
        'cuestionarios_combinados': cuestionarios_combinados,
    }
    
    # Renderizar la plantilla con el contexto que contiene los cuestionarios
    return render(request, 'integradora/vista_integrada.html', context)

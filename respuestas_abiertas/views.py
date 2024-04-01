from django.shortcuts import render, get_object_or_404, redirect
from .models import CuestionarioAbierto, PreguntaAbierta

def lista_cuestionarios(request):
    cuestionarios = CuestionarioAbierto.objects.all()
    return render(request, 'respuestas_abiertas/lista_cuestionarios.html', {'cuestionarios': cuestionarios})

def cuestionario_detalle(request, pk):
    cuestionario = get_object_or_404(CuestionarioAbierto, pk=pk)
    if request.method == 'POST':
        # Aquí podrías procesar las respuestas. Por simplicidad, redirigimos al mismo cuestionario.
        return redirect('respuestas_abiertas:cuestionario_detalle', pk=cuestionario.pk)
    return render(request, 'respuestas_abiertas/cuestionario_detalle.html', {'cuestionario': cuestionario})

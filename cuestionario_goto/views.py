from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .models import Pregunta, Respuesta
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from io import BytesIO


def cuestionario_completo_view(request):
    """
    Esta vista muestra una lista completa de preguntas como parte de un cuestionario general,
    sin detalles individuales por pregunta.
    """
    if request.method == 'POST':
        # Obtener las respuestas del formulario
        respuestas_usuario = {key: request.POST[key] for key in request.POST.keys() if key.startswith('respuesta_')}
        
        # Verificar si hay al menos una respuesta
        if not respuestas_usuario:
            return HttpResponse("Por favor, selecciona al menos una respuesta.")

        # Generar el PDF con las respuestas
        pdf_content = generar_pdf(respuestas_usuario)

        # Enviar correo con el PDF adjunto
        enviar_email(pdf_content, "Resultado del Cuestionario", "Aquí está el PDF con tus respuestas al cuestionario.", ['carlos.jimenez@nephosit.com'])

        return HttpResponse("Gracias por completar el cuestionario. Las respuestas han sido enviadas por correo electrónico.")
    else:
        preguntas = Pregunta.objects.all()
        return render(request, 'cuestionario_goto/cuestionario.html', {'preguntas': preguntas})

def detalle_pregunta_view(request, pregunta_id):
    """
    Esta vista maneja la visualización de detalles para una pregunta individual,
    accesible a través de un ID de pregunta específico.
    """
    pregunta = get_object_or_404(Pregunta, id=pregunta_id)
    respuestas = Respuesta.objects.filter(pregunta=pregunta)
    return render(request, 'cuestionario_goto/detalle_pregunta.html', {'pregunta': pregunta, 'respuestas': respuestas})

def cuestionario_view(request):
    """
    Redirige a la vista del cuestionario completo.
    """
    return redirect('cuestionario_goto:cuestionario_completo')

def generar_pdf(respuestas_usuario):
    """
    Genera un PDF basado en las respuestas del usuario a las preguntas del cuestionario.
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Estilo para las preguntas
    estilo_pregunta = styles['BodyText']
    estilo_pregunta.spaceAfter = 0.1 * inch
    estilo_pregunta.spaceBefore = 0.2 * inch
    estilo_pregunta.fontSize = 12
    estilo_pregunta.leading = 16

    # Estilo para las respuestas
    estilo_respuesta = styles['BodyText']
    estilo_respuesta.leftIndent = 20
    estilo_respuesta.fontSize = 10
    estilo_respuesta.leading = 14

    for pregunta_id, respuesta_id in respuestas_usuario.items():
        pregunta = Pregunta.objects.get(id=int(pregunta_id.split('_')[1]))
        respuesta = Respuesta.objects.get(id=int(respuesta_id))

        # Agregar la pregunta al PDF
        story.append(Paragraph(f"Pregunta: {pregunta.texto}", estilo_pregunta))

        # Agregar la respuesta al PDF
        story.append(Paragraph(f"Respuesta: {respuesta.texto}", estilo_respuesta))

        # Agregar espacio entre cada pregunta y respuesta
        story.append(Spacer(1, 12))

    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf


def enviar_email(content, subject, message, recipient_list):
    """
    Envia un email al usuario con el PDF adjunto que contiene las respuestas del cuestionario.
    """
    email = EmailMessage(
        subject,
        message,
        'carlos.jimenez@nephosit.com',  # Consider changing 'from@example.com' to your actual sender email
        recipient_list
    )
    email.attach('cuestionario_respuestas.pdf', content, 'application/pdf')
    email.send(fail_silently=False)

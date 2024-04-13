from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Cuestionario, Pregunta
from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from io import BytesIO

def lista_cuestionarios(request):
    cuestionarios = Cuestionario.objects.all()
    return render(request, 'cuestionarios_combinados/lista_cuestionarios.html', {'cuestionarios': cuestionarios})

def detalle_cuestionario(request, cuestionario_id):
    cuestionario = get_object_or_404(Cuestionario, id=cuestionario_id)
    return render(request, 'cuestionarios_combinados/detalle_cuestionario.html', {'cuestionario': cuestionario})

def procesar_respuestas(request, cuestionario_id):
    if request.method == 'POST':
        cuestionario = get_object_or_404(Cuestionario, id=cuestionario_id)
        respuestas = []
        for pregunta in cuestionario.pregunta_set.all():
            if pregunta.abierta:
                respuesta_texto = request.POST.get(f'respuesta_abierta_{pregunta.id}', '')
            else:
                respuesta_texto = request.POST.get(f'respuesta_{pregunta.id}', '')
            respuestas.append((pregunta.texto, respuesta_texto))  # Store as tuple

        pdf = generar_pdf_cuestionario_como_objeto(cuestionario, respuestas)
        enviar_cuestionario_por_email(cuestionario, pdf)
        return HttpResponse("Gracias por completar el cuestionario. Ha sido enviado correctamente.")
    else:
        return HttpResponse("Invalid request", status=400)

def enviar_cuestionario_por_email(cuestionario, pdf):
    email = EmailMessage(
        'Cuestionario Completado',   # Subject
        'Aquí está el cuestionario que ha completado.',  # Message
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.DEFAULT_TO_EMAIL]
    )
    email.attach(f'{cuestionario.titulo}.pdf', pdf.getvalue(), 'application/pdf')
    pdf.close()
    email.send()

def generar_pdf_cuestionario_como_objeto(cuestionario, respuestas):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    Story = []
    styles = getSampleStyleSheet()

    title_style = styles['Title']
    title_style.alignment = 1  # Center align title
    title = Paragraph(f'<b>Cuestionario: {cuestionario.titulo}</b>', title_style)
    Story.append(title)
    Story.append(Spacer(1, 24))  # More space after the title

    question_style = styles['BodyText']
    question_style.fontSize = 11
    answer_style = styles['BodyText']
    answer_style.fontSize = 10

    for pregunta, respuesta in respuestas:
        pregunta_para = Paragraph(f'<b>Pregunta:</b> {pregunta}', question_style)
        respuesta_para = Paragraph(f'<b>Respuesta:</b> {respuesta}', answer_style)
        Story.append(pregunta_para)
        Story.append(Spacer(1, 6))  # Less space between question and answer
        Story.append(respuesta_para)
        Story.append(Spacer(1, 18))  # More space before next question

    doc.build(Story)
    buffer.seek(0)
    return buffer

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage
from .models import CuestionarioAbierto, PreguntaAbierta
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit
from io import BytesIO

def lista_cuestionarios(request):
    cuestionarios = CuestionarioAbierto.objects.all()
    return render(request, 'respuestas_abiertas/lista_cuestionarios.html', {'cuestionarios': cuestionarios})

def cuestionario_detalle(request, pk):
    cuestionario = get_object_or_404(CuestionarioAbierto, pk=pk)

    if request.method == 'POST':
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter  # Dimensions of the page
        p.setFont("Helvetica", 12)  # Set the font and size
        margin = 72  # Set a margin of 1 inch
        y = height - margin  # Start near the top of the page

        for pregunta in cuestionario.preguntaabierta_set.all():
            question_text = f"Pregunta: {pregunta.texto_pregunta}"
            lines = simpleSplit(question_text, "Helvetica", 12, width - 2 * margin)  # Wrap text
            for line in lines:
                p.drawString(margin, y, line)
                y -= 14  # Move to the next line

            # Fetch the response, ensure it's a string and wrap it
            respuesta = request.POST.get(f'pregunta_{pregunta.id}', 'No respondida')
            response_text = f"Respuesta: {respuesta}"
            response_lines = simpleSplit(response_text, "Helvetica", 12, width - 2 * margin)
            y -= 14  # Leave a small space between question and answer
            for line in response_lines:
                p.drawString(margin, y, line)
                y -= 14  # Move to the next line

            y -= 20  # Additional space before the next Q&A pair

            if y < margin + 50:  # Avoid writing too close to the bottom of the page
                p.showPage()
                y = height - margin

        p.showPage()
        p.save()

        pdf = buffer.getvalue()
        buffer.close()

        email = EmailMessage(
            'Respuesta a Cuestionario',
            'Por favor encuentra adjunto el PDF con las respuestas al cuestionario.',
            'carlos.jimenez@nephosit.com',
            ['carlos.jimenez@nephosit.com'],
            reply_to=['carlos.jimenez@nephosit.com'],
        )
        email.attach('respuesta_cuestionario.pdf', pdf, 'application/pdf')
        email.send()

        return redirect('respuestas_abiertas:respuesta_exitosa')

    return render(request, 'respuestas_abiertas/cuestionario_detalle.html', {'cuestionario': cuestionario})

def respuesta_exitosa(request):
    return render(request, 'respuestas_abiertas/respuesta_exitosa.html')

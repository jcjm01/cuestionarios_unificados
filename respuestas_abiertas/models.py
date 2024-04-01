from django.db import models

class CuestionarioAbierto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

class PreguntaAbierta(models.Model):
    cuestionario = models.ForeignKey(CuestionarioAbierto, on_delete=models.CASCADE)
    texto_pregunta = models.CharField(max_length=200)

    def __str__(self):
        return self.texto_pregunta

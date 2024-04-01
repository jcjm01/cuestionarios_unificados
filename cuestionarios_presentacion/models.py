from django.db import models

class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    def __str__(self):
        return self.texto

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    siguiente_pregunta = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

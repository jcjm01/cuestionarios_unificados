from django.db import models

# Create your models here.
from django.db import models

class Pregunta(models.Model):
    texto = models.TextField()

    def __str__(self):
        return self.texto

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.TextField()
    valor = models.IntegerField(default=0)  # Asigna valores a las respuestas

    def __str__(self):
        return f"{self.texto} ({self.valor})"

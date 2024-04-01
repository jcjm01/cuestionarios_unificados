from django.db import models

class Cuestionario(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    def __str__(self):
        return self.titulo

class Pregunta(models.Model):
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    abierta = models.BooleanField(default=False)
    def __str__(self):
       return self.texto
    
class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    def __str__(self):
        return self.texto
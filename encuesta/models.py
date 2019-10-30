from django.db import models
from django.contrib.auth.models import User

class Imagen(models.Model):
    """"Upload the image to be voted. The uploaded images are saved in a gallery"""
    image = models.ImageField(upload_to = 'encuesta', default = 'static/Scatter_Mh_vs_Ms.png')
    name = models.CharField(max_length=200)

class Choice(models.Model):
    """"For a uploaded image, allow select between three different types one to classify it"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE,  blank=True, null=True)
    CHOICE_TEXT = (('A', 'Alta'), ('B', 'Baja'), ('C','Ninguna'))
    voto = models.CharField(max_length=200, choices=CHOICE_TEXT)
    

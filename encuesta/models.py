from django.db import models

# Create your models here.
class Imagen(models.Model):
    """"Upload the image to be voted. The uploaded images are saved in a gallery"""
    image = models.ImageField(upload_to = 'encuesta', default = 'img1.jpeg')
    name = models.CharField(max_length=200)

class Choice(models.Model):
    """"For a uploaded image, allow select between three different types one to classify it"""
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE,  blank=True, null=True)
    CHOICE_TEXT = (('A', 'Alta'), ('B', 'Baja'), ('C','Ninguna'))
    voto = models.CharField(max_length=200, choices=CHOICE_TEXT)
    

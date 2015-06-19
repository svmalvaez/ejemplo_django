from django.db import models

class Persona(models.Model):
	nombre = models.CharField(max_length=30)
	telefono = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	direccion = models.TextField(max_length=100)

from django.db import models

# Create your models here.

opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Agradecimiento"]
]

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='productos', null=True)
    precio = models.IntegerField()
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensajes = models.TextField() 
    def __str__(self):
        return self.nombre
    


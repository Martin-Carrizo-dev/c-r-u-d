from django.db import models

class Task(models.Model):  # Llamo a models
    title = models.CharField(max_length=100)  # Titulo - maximo 100 caracteres
    description = models.TextField(blank=True)  # descripcion de las tareas - puede venir en blanco
    is_completed = models.BooleanField(default=False)  # agrego booleano para permitir controlar si la tarea esta completa - por defecto false
    created = models.DateField(auto_now=True)  # sirve para mantener un orden de las tareas cuando las creemos - guarda automaticamente la fecha, saca la fecha de la zona horaria ya definida
     #
    
    class Meta:
        ordering = ['-created']  # creo la columa created que me sirve para ordenar los valores de las tareas creadas

def __str__(self):
    return self.title  # imprime el título de la tarea al momento de crearla - sirve principalmente al programador
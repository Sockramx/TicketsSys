from django.db import models

# Create your models here.

class Prioridad(models.Model):
    prioridad = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return self.prioridad


class Ticket(models.Model):
    asunto = models.CharField(max_length=200, blank=False)
    descripcion = models.TextField(max_length=400, blank=False)
    prioridad = models.ForeignKey('Prioridad', on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.asunto
        
  
    

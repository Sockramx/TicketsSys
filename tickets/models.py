from django.db import models

# Create your models here.

class Ticket(models.Model):
    nombre = models.CharField(max_length=40)
    

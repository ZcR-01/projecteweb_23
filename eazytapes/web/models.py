from django.db import models

# Create your models here. Base de dades; Controller - Python (logical business)
# Escrit en python pero el django ho tradueix a sql

class Bar(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    

class Tapa(models.Model):
    name = models.CharField(max_length=200)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE) # Clau forana que apunta a bar, si es borra el bar tambe es borrara
    #la tapa

    def __str__(self) -> str:
        return self.name+" del "+self.bar.name
    

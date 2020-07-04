from django.db import models

# Create your models here.

# Create your models here.
class Example1(models.Model):
    
    name = models.CharField(max_length= 200, null = False, default = "Null")
    edad = models.CharField(max_length= 200, null = False, default = "Null")
    direccion = models.CharField(max_length= 200, null = False, default = "Null")
    curp = models.CharField(max_length= 200, null = False, default = "Null")


    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'Example1'
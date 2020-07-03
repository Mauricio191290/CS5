from django.db import models

# Create your models here.

class Example1(models.Model):
    name= models.CharField(max_length = 255,null = False)
    edad = models.CharField(max_length=2,null = False)
    direccion = models.CharField(max_length = 200,null = False)
    curp = models.CharField(max_length = 16, null = False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Example1'

    
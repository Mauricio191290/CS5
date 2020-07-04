from django.db import models

# Create your models here.

class Example1(models.Model):
    name= models.CharField(max_length = 255,null = False, default = 'null')
    edad = models.CharField(max_length=2,null = False, default = 'null')
    direccion = models.CharField(max_length = 200,null = False, default = 'null')
    curp = models.CharField(max_length = 16, null = False, default = 'null')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Example1'

    
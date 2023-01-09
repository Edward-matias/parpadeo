from django.db import models

# Create your models here.
class post(models.Model):
    fecha= models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.
class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nome_documento = models.TextField(max_length=255)
    data_modificacao = models.DateField(auto_now=True)
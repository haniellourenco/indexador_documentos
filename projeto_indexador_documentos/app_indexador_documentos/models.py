from django.db import models
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # Obtém a extensão do arquivo
    valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Tipo de arquivo não suportado. Por favor, envie um arquivo PDF, JPG, JPEG ou PNG.')


# Create your models here.
class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nome_documento = models.TextField(max_length=100)
    data_modificacao = models.DateField(auto_now=True)
    arquivo = models.FileField(upload_to='documentos/', validators=[validate_file_extension])


    def __str__(self):
        return self.nome_documento
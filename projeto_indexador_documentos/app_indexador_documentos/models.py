from django.db import models
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger('app_indexador_documentos')

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # Obtém a extensão do arquivo
    valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        logger.warning(f'Tentativa de upload de arquivo com extensão inválida: {ext}')
        raise ValidationError('Tipo de arquivo não suportado. Por favor, envie um arquivo PDF, JPG, JPEG ou PNG.')

class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nome_documento = models.TextField(max_length=100)
    data_modificacao = models.DateField(auto_now=True)
    arquivo = models.FileField(upload_to='documentos/', validators=[validate_file_extension])

    def __str__(self):
        return self.nome_documento

    def save(self, *args, **kwargs):
        logger.info(f'Salvando documento: {self.nome_documento}')
        try:
            super().save(*args, **kwargs)
            logger.debug(f'Documento salvo com sucesso. ID: {self.id_documento}')
        except Exception as e:
            logger.error(f'Erro ao salvar documento: {str(e)}', exc_info=True)
            raise

    def delete(self, *args, **kwargs):
        logger.info(f'Excluindo documento: {self.nome_documento} (ID: {self.id_documento})')
        try:
            super().delete(*args, **kwargs)
            logger.debug(f'Documento excluído com sucesso. ID: {self.id_documento}')
        except Exception as e:
            logger.error(f'Erro ao excluir documento: {str(e)}', exc_info=True)
            raise
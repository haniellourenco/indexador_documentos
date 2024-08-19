from django.shortcuts import render, redirect
from .models import Documento
from .forms import DocumentoForm
import logging

logger = logging.getLogger('app_indexador_documentos')

def home(request):
    logger.info('Acessando a página inicial')
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        logger.debug('Formulário submetido na página inicial')
        if form.is_valid():
            logger.info('Formulário válido, salvando novo documento')
            try:
                form.save()
                logger.info('Documento salvo com sucesso')
                return redirect('listagem_documentos')
            except Exception as e:
                logger.error(f'Erro ao salvar documento: {str(e)}', exc_info=True)
                return render(request, 'documentos/home.html', {'form': form, 'error': 'Erro ao salvar documento'})
        else:
            logger.warning('Formulário inválido submetido')
    else:
        form = DocumentoForm()
    
    return render(request, 'documentos/home.html', {'form': form})

def documentos(request):
    logger.info('Acessando a listagem de documentos')
    try:
        documentos = Documento.objects.all()
        logger.debug(f'Recuperados {documentos.count()} documentos')
        return render(request, 'documentos/documentos.html', {'documentos': documentos})
    except Exception as e:
        logger.error(f'Erro ao recuperar documentos: {str(e)}', exc_info=True)
        return render(request, 'documentos/documentos.html', {'error': 'Erro ao carregar documentos'})

def editar(request, id):
    logger.info(f'Acessando edição do documento ID: {id}')
    try:
        documento = Documento.objects.get(id_documento=id)
        if request.method == 'POST':
            form = DocumentoForm(request.POST, request.FILES, instance=documento)
            logger.debug('Formulário de edição submetido')
            if form.is_valid():
                form.save()
                logger.info(f'Documento ID: {id} atualizado com sucesso')
                return redirect('listagem_documentos')
            else:
                logger.warning(f'Formulário inválido na edição do documento ID: {id}')
        else:
            form = DocumentoForm(instance=documento)
        
        return render(request, 'documentos/update.html', {'form': form, 'documento': documento})
    except Documento.DoesNotExist:
        logger.error(f'Tentativa de editar documento inexistente ID: {id}')
        return redirect('listagem_documentos')
    except Exception as e:
        logger.error(f'Erro ao editar documento ID: {id}: {str(e)}', exc_info=True)
        return render(request, 'documentos/update.html', {'error': 'Erro ao editar documento'})

def delete(request, id):
    logger.info(f'Solicitação de exclusão do documento ID: {id}')
    try:
        documento = Documento.objects.get(id_documento=id)
        documento.delete()
        logger.info(f'Documento ID: {id} excluído com sucesso')
        return redirect('listagem_documentos')
    except Documento.DoesNotExist:
        logger.error(f'Tentativa de excluir documento inexistente ID: {id}')
        return redirect('listagem_documentos')
    except Exception as e:
        logger.critical(f'Erro crítico ao excluir documento ID: {id}: {str(e)}', exc_info=True)
        return render(request, 'documentos/documentos.html', {'error': 'Erro ao excluir documento'})
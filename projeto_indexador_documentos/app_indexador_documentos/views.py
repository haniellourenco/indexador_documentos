from django.shortcuts import render
from .models import Documento

def home(request):
    return render(request,'documentos/home.html')

def documentos(request):
    if request.method == 'POST':
        # Salvar os dados da tela para o banco de dados
        novo_documento = Documento()
        novo_documento.nome_documento = request.POST.get('nome')
        novo_documento.data_modificacao = request.POST.get('data')
        novo_documento.save()
    
    # Exibir todos os documentos já inseridos em uma nova página
    documentos = {
        'documentos': Documento.objects.all()
    }
    # Retornar os dados para a página de listagem de documentos
    return render(request, 'documentos/documentos.html', documentos)
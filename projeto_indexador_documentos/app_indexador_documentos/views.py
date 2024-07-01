from django.shortcuts import render, redirect
from .models import Documento
from .forms import DocumentoForm

def home(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listagem_documentos')
    else:
        form = DocumentoForm()
    
    return render(request, 'documentos/home.html', {'form': form})


def documentos(request):
    documentos = {
        'documentos': Documento.objects.all()
    }
    return render(request, 'documentos/documentos.html', documentos)

def editar(request, id):
    documento = Documento.objects.get(id_documento=id)
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES, instance=documento)
        if form.is_valid():
            form.save()
            return redirect('listagem_documentos')
    else:
        form = DocumentoForm(instance=documento)
    
    return render(request, 'documentos/update.html', {'form': form, 'documento': documento})

def delete(request, id):
    documento = Documento.objects.get(id_documento=id)
    documento.delete()
    return redirect('listagem_documentos')

from django import forms
from .models import Documento

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['nome_documento', 'arquivo']
        widgets = {
            'nome_documento': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control form-control-sm'}),
        }

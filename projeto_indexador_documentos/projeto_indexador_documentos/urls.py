from django.urls import path
from app_indexador_documentos import views

urlpatterns = [
    # rota, view responsável, nome de referência
    path('', views.home, name='home'),
    path('documentos/', views.documentos, name='listagem_documentos'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('update/<int:id>', views.update, name='update'),
]

from django.urls import path
from app_indexador_documentos import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('documentos/', views.documentos, name='listagem_documentos'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('delete/<int:id>', views.delete, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from app_cadastro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('usuarios/editar/<int:id_usuario>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:id_usuario>/', views.excluir_usuario, name='excluir_usuario'),
    path('usuarios/confirmar-excluir-todos/', views.confirmar_excluir_todos, name='confirmar_excluir_todos'),
    path('usuarios/excluir-todos/', views.excluir_todos, name='excluir_todos'),
]

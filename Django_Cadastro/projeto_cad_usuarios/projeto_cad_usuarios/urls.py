from django.urls import path
from app_cad_usuarios import views

urlpatterns =[
    # rota, view referente, nome de referência
    path('', views.home, name='home'),
    # usuarios.com/usuarios
    path('usuario/', views.usuarios,name='listagem_usuarios')]

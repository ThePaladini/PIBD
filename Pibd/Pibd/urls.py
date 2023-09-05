from django.urls import path
from django.contrib import admin
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world, name='hello_world'),
    path('insert_info/', views.insert, name='insert_info'),
    path('cadastro_ies/', views.cadastro_ies, name='cadastro_ies'),
    path('registro_coordenador_administrativo/', views.registro_coordenador_administrativo, name='registro_coordenador_administrativo'),
    path('data_coord_admin/', views.data_coord_admin, name='data_coord_admin'),
    
]
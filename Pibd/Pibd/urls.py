from django.urls import path
from django.contrib import admin
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_info/', views.insert, name='insert_info'),
    path('cadastro_ies/', views.cadastro_ies, name='cadastro_ies'),
    path('registro_coordenador_administrativo/', views.registro_coordenador_administrativo, name='registro_coordenador_administrativo'),
    path('data_coord_admin/', views.data_coord_admin, name='data_coord_admin'),
    path('comp_curriculares/', views.comp_curriculares, name='comp_curriculares'),
    path('lista_oferta_coletiva/', views.lista_oferta_coletiva, name='lista_oferta_coletiva'),
    path('data_test/', views.view_data, name='data_test'),
    path('create_ies/', views.create_ies, name='create_ies'),
    path('turma_esp_doc_autor', views.turma_esp_doc_autor, name='turma_esp_doc_autor'),
]
    
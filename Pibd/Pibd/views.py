from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return render(request, 'hello.html')

def insert(request):
    return render(request, 'alter_info_professor_ministrante.html')    

def cadastro_ies(request):
    return render(request, 'cadastro_ies.html')

def registro_coordenador_administrativo(request):
    return render(request, 'registro_coordenador_administrativo.html')
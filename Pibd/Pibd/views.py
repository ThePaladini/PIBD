from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def hello_world(request):
    return render(request, 'hello.html')

def insert(request):
    return render(request, 'alter_info_professor_ministrante.html')    

def cadastro_ies(request):
    return render(request, 'cadastro_ies.html')

def registro_coordenador_administrativo(request):
    return render(request, 'registro_coordenador_administrativo.html')

def data_coord_admin(request):
    return render(request, 'data_coord_admin.html')

def comp_curriculares(request):
    return render(request, 'comp_curriculares.html')

def lista_oferta_coletiva(request):
    return render(request, 'lista_oferta_coletiva.html')

    context = {
        'page_title': 'Admin Dashboard',
        'user_name': 'John Doe',
        'num_users': 500,
        'recent_data_points': [
            {'date': '2023-09-01', 'value': 120},
            {'date': '2023-09-02', 'value': 150},
            {'date': '2023-09-03', 'value': 180},
            {'date': '2023-09-04', 'value': 140},
            {'date': '2023-09-05', 'value': 160},
        ],
        'active_users': [
            'User1', 'User2', 'User3', 'User4', 'User5'
        ]
    }
    return render(request, 'data_coord_admin.html', context)


def view_data(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM vw_turma_especializacao_agrupada')
        data = cursor.fetchall()

    # Process the data as needed
    # For example, you can convert it into a list of dictionaries

    context = {'data': data}
    return render(request, 'data_template.html', context)


def create_ies(request):
    success_message = None
    error_message = None

    if request.method == 'POST':
        nome_ies = request.POST.get('nome-ies')
        sigla = request.POST.get('sigla')
        campus = request.POST.get('campus')
        cnpj = request.POST.get('cnpj')
        logradouro = request.POST.get('logradouro')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        estado = request.POST.get('estado')
        pais = request.POST.get('pais')
        numero = request.POST.get('numero')
        cep = request.POST.get('cep')
        ddi = request.POST.get('ddi')
        ddd = request.POST.get('ddd')
        numero_telefone = request.POST.get('numero-telefone')
        nucli = request.POST.get('nucli')
        labmaisunidos = request.POST.get('labmaisunidos')
        link_politica = request.POST.get('link-politica')
        data_politica = request.POST.get('data-politica')


        # Define your SQL queries based on the form data
        endereco_query = "INSERT INTO cep_endereco (cep, rua, bairro, cidade, estado, pais) VALUES (%s, %s, %s, %s, %s, %s)"
        ies_query = "INSERT INTO ies (cnpj, sigla, participou_isf, tem_lab_mais_unidos, possui_nucleo_ativo, cep_ies, numero, complemento, link_politica_ling, data_politica_ling, doc_politica_ling, campus, nome_principal) VALUES (%s, %s, true, true, true, %s, %s, %s, %s, %s, '', %s, %s)"
        telefone_query = "INSERT INTO telefone_ies (cnpj_ies, ddi, ddd, numero) VALUES (%s ,%s, %s, %s)"

        # Execute the SQL queries
        with connection.cursor() as cursor:
            try:
                cursor.execute(endereco_query, (cep, logradouro, bairro, 'Cidade A', estado, pais))
                cursor.execute(ies_query, (cnpj, sigla, cep, numero, complemento, link_politica, data_politica, campus, nome_ies))
                cursor.execute(telefone_query, (cnpj ,ddi, ddd, numero_telefone))

                # If all queries are successful, set success_message
                success_message = "IES created successfully."
            except Exception as e:
                # If there's an error, set error_message
                error_message = f"Failed to create IES: {str(e)}"

    return render(request, 'cadastro_ies.html', {'success_message': success_message, 'error_message': error_message})


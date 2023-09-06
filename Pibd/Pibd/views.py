from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from datetime import date

def main(request):
    return render(request, 'index.html')

def insert_professor_ministrante(request):
    return render(request, 'alter_info_professor_ministrante.html')

def turma_esp(request):
    return render(request, 'view_turma_esp.html')

def cadastro_ies(request):
    return render(request, 'cadastro_ies.html')

def registro_coordenador_administrativo(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM coordenador_administrativo where coordenador_administrativo.cpf_coordenador = \'98765432101\'')
        results = cursor.fetchall()
    context = {'results': results, 'data': results[0][3].strftime('%Y-%m-%d')}
    return render(request, 'registro_coordenador_administrativo.html', context)


def registrar_coordenador_administrativo(request):
    success_message = None
    error_message = None
    if request.method == 'POST':
        func = request.POST.get('func')
        curriculo = request.POST.get('curiculo')
        data = request.POST.get('data')
        poca = request.POST.get('poca')
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM coordenador_administrativo where coordenador_administrativo.cpf_coordenador = \'98765432101\'')
            results = cursor.fetchall()

                    # Define your SQL queries based on the form data
            query = """CALL proc_atualizar_coordenador_administrativo(
                                            '98765432101',                -- cpf_coordenador_param
                                            %s::VARCHAR,               -- funcao_na_instituicao_param
                                            %s::VARCHAR, -- curriculo_lates_param
                                            %s::DATE,                -- data_cadastro_param (date in 'YYYY-MM-DD' format)
                                            %s::VARCHAR                    -- poca_param
                                        );"""    
            args = (func, curriculo, data, poca)

            # Execute the SQL queries
            with connection.cursor() as cursor:
                try:
                    cursor.execute(query, args)
                    # If all queries are successful, set success_message
                    success_message = "coordenador altered successfully."
                except Exception as e:
                    # If there's an error, set error_message
                    error_message = f"Failed to alter coordenador: {str(e)}"   
    return render(request, 'registro_coordenador_administrativo.html', {'success_message': success_message, 'error_message': error_message})

def data_coord_admin(request):
    
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

def comp_curriculares(request):
    view = 'componente_curricular'

    if request.method == 'GET':
        if request.GET.get('dropdown') == '1':
            view = 'apresenta_componentes_por_idioma'
        elif request.GET.get('dropdown') == '2':
            view = 'apresenta_componentes_por_carga_teorica'
        elif request.GET.get('dropdown') == '3':
            view = 'apresenta_componentes_por_carga_pratica'
        elif request.GET.get('dropdown') == '4':
            view = 'apresenta_componentes_por_eixo_tematico'

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM ' + view)
        results = cursor.fetchall()

    context = {'results': results, 'selected_value': request.GET.get('dropdown')}
    return render(request, 'comp_curriculares.html', context)

def lista_oferta_coletiva(request):
    return render(request, 'lista_oferta_coletiva.html')


def view_data(request): #for tests
    view = 'apresenta_componentes_por_carga_teorica'
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM ' + view)
        results = cursor.fetchall()

    context = {'results': results}
    return render(request, 'comp_curriculares.html', context)


def create_ies(request):
    success_message = None
    error_message = None

    if request.method == 'POST':
        nome_ies = request.POST.get('nome-ies')
        participou_isf = request.POST.get('participou-Isf') == 'on'
        sigla = request.POST.get('sigla')
        campus = request.POST.get('campus')
        cnpj = request.POST.get('cnpj')
        rua = request.POST.get('logradouro')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        pais = request.POST.get('pais')
        numero = request.POST.get('numero')
        cep = request.POST.get('cep')
        ddi = request.POST.get('ddi')
        ddd = request.POST.get('ddd')
        numero_telefone = request.POST.get('numero-telefone')
        nucli = request.POST.get('nucli') == 'on'
        labmaisunidos = request.POST.get('labmaisunidos') == 'on'
        link_politica = request.POST.get('link-politica')
        data_politica = request.POST.get('data-politica')
        documento_politica = "C:/path/para/arquivo/documento.pdf"


        # Define your SQL queries based on the form data
        query = """CALL proc_cadastra_ies(%s::VARCHAR, %s::VARCHAR, %s::BOOLEAN, %s::BOOLEAN, %s::BOOLEAN, %s::VARCHAR, 
                    %s::VARCHAR, %s::VARCHAR, %s::VARCHAR, %s::VARCHAR, %s::VARCHAR, %s::INTEGER, %s::VARCHAR, %s::VARCHAR, 
                    %s::DATE, %s::VARCHAR, %s::VARCHAR, %s::VARCHAR, %s::VARCHAR, %s::VARCHAR, %s::VARCHAR)"""    
        args = (cnpj, sigla, participou_isf, labmaisunidos, nucli, cep, rua, bairro, 
                cidade, estado, pais, numero, complemento, link_politica, data_politica,
                documento_politica, campus, nome_ies, ddd, ddi, numero_telefone)

        # Execute the SQL queries
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, args)
              
                # If all queries are successful, set success_message
                success_message = "IES created successfully."
            except Exception as e:
                # If there's an error, set error_message
                error_message = f"Failed to create IES: {str(e)}"

    return render(request, 'cadastro_ies.html', {'success_message': success_message, 'error_message': error_message})

def turma_esp_doc_autor(request):
    return render(request, 'turma_esp_doc_autor.html')


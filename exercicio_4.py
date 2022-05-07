import pytest
import csv
import main

def ler_dados_csv():
    dados_csv = []
    nome_arquivo = 'massas_de_teste/exercicio_4.csv'
    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            campos = csv.reader(arquivo_csv, delimiter=';')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo nao encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha nao prevista: {fail}')

@pytest.mark.parametrize('lado_da_base, altura_inclinada, resultado_esperado, tipo_teste', ler_dados_csv())
def teste_calcular_area_piramide_quadrangular(lado_da_base, altura_inclinada, resultado_esperado, tipo_teste):
    # Configura
    # Valores vem da massa de teste

    # Executa
    resultado_obtido = main.calcular_area_piramide_quadrangular(int(lado_da_base), int(altura_inclinada))

    # Valida
    if tipo_teste == 'positivo':
        assert float(resultado_esperado) == resultado_obtido
    else:
        assert resultado_esperado == resultado_obtido




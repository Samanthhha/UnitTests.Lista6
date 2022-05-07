import pytest
import main

lista_para_calcular_paralelogramo = [
    (10, 15, 150),
    (7, 0, 'um ou ambos os valores de base e altura sao zero ou negativos'),
    (5, -7, 'um ou ambos os valores de base e altura sao zero ou negativos'),
    (6, 'a', 'um ou ambos os valores de base e altura sao letras')
]


@pytest.mark.parametrize('base, altura, resultado_esperado', lista_para_calcular_paralelogramo)
def teste_calcular_area_paralelogramo(base, altura, resultado_esperado):
    # Configura vem da lista

    # Executa
    resultado_obtido = main.calcular_area_paralelogramo(base, altura)

    # Valida
    assert resultado_esperado == resultado_obtido



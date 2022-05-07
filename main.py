def eh_numero(candidato):
    try:
        float(candidato)
    except ValueError:
        return False    # se é texto (string)
    return True         # se é numero (float)

def calcular_area_cubo(lado):
    # area do cubo eh igual a area do lado vezes 6
    if eh_numero(lado):
        if lado > 0:
            return (lado ** 2) * 6
        else:
            return 'Valor do lado zero ou negativo'
    else:
        return 'lado eh letra'


def calcular_area_paralelogramo(base, altura):
    if eh_numero(base) and eh_numero(altura):
        if base > 0 and altura > 0:
             return base * altura
        else:
            return 'um ou ambos os valores de base e altura sao zero ou negativos'
    else:
        return 'um ou ambos os valores de base e altura sao letras'

def calcular_area_piramide_quadrangular(lado_da_base, altura_inclinada):
    if eh_numero(lado_da_base) and eh_numero(altura_inclinada):
        if lado_da_base > 0 and altura_inclinada > 0:
            area_da_base = lado_da_base ** 2
            area_do_triangulo = (lado_da_base * altura_inclinada) / 2
            return area_da_base + (4 * area_do_triangulo)
        else:
            return 'um ou ambos os valores do lado_da_base e da altura_inclinada sao zero ou negativos'
    else:
        return 'um ou ambos os valores do lado_da_base e da altura_inclinada sao letras'



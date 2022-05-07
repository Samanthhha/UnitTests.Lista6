import unittest
import main


class MyTestCase(unittest.TestCase):
    def testar_area_cubo_positivo(self):
        resultado_esperado = 150
        resultado_obtido = main.calcular_area_cubo(5)
        self.assertEqual(resultado_obtido, resultado_esperado)

    def testar_area_cubo_negativo(self):
        resultado_negativo = 'Valor do lado zero ou negativo'
        resultado_obtido = main.calcular_area_cubo(-5)
        self.assertEqual(resultado_obtido, resultado_negativo)



if __name__ == '__main__':
    unittest.main()

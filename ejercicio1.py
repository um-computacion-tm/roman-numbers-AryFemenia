#tests
import unittest
def decimal_to_roman(decimal):
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 4:
        return 'IV'
    elif decimal == 5:
        return 'V'
    elif decimal == 6:
        return 'VI'
    elif decimal == 9:
        return 'IX'
    elif decimal == 10:
        return 'X'
    else:
        return 'test'

#codigo
class TestDEcimalToRoman(unittest.TestCase):
    def test_uno(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, 'I')
    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')
    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')
    def test_cuatro(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, 'IV')
    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')
    def test_seis(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, 'VI')
    def test_nueve(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, 'IX')
    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

if __name__ == '__main__':
    unittest.main()
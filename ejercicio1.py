import unittest

#tests
def decimal_to_roman(decimal):
    resultado = ''
    if decimal >= 1000:
        resultado = 'M'
        decimal -= 1000
    if decimal >= 100:
        centenas = decimal // 100
        decimal -= centenas * 100
        if centenas <= 3:
            centenas = 'C' * centenas
        elif centenas == 4:
            centenas += 'CD'
        elif centenas <= 8:
            centenas += 'D' + (centenas - 5) * 'C'
        elif centenas <= 9:
            resultado += 'CM'
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 4:
        return 'IV'
    elif decimal <= 8:
        resultado += 'V' + (decimal - 5) * 'I'
    elif decimal == 9:
        return 'IX'
    elif decimal == 10:
        return 'X'
    else:
        return resultado

#codigo
class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_to_roman(1)
        # verificacion
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

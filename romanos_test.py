#IMPORTS
import unittest
from romanos import decimal_to_roman, roman_to_decimal

#TEST DEC TO ROM
class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, 'I')
    def test_2(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')
    def test_3(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')
    def test_4(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, 'IV')
    def test_5(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')
    def test_6(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, 'VI')
    def test_7(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, 'VII')
    def test_7(self):
        resultado = decimal_to_roman(8)
        self.assertEqual(resultado, 'VIII')
    def test_9(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, 'IX')
    def test_10(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')
    def test_50(self):
        resultado = decimal_to_roman(50)
        self.assertEqual(resultado, 'L')
    def test_90(self):
        resultado = decimal_to_roman(90)
        self.assertEqual(resultado, 'XC')
    def test_100(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C')
    def test_101(self):
        resultado = decimal_to_roman(101)
        self.assertEqual(resultado, 'CI')
    def test_123(self):
        resultado = decimal_to_roman(123)
        self.assertEqual(resultado, 'CXXIII')
    def test_456(self):
        resultado = decimal_to_roman(456)
        self.assertEqual(resultado, 'CDLVI')
    def test_987(self):
        resultado = decimal_to_roman(987)
        self.assertEqual(resultado, 'CMLXXXVII')    
    def test_1000(self):
        resultado = decimal_to_roman(1000)
        self.assertEqual(resultado, 'M')

#TEST ROM TO DEC
class TestRomanToDecimal(unittest.TestCase):
    def test_CXXIII(self):
        resultado = roman_to_decimal('CXXIII')
        self.assertEqual(resultado, 123)
    def test_I(self):
        resultado = roman_to_decimal('I')
        self.assertEqual(resultado, 1)
    def test_II(self):
        resultado = roman_to_decimal('II')
        self.assertEqual(resultado, 2)
    def test_III(self):
        resultado = roman_to_decimal('III')
        self.assertEqual(resultado, 3)
    def test_IV(self):
        resultado = roman_to_decimal('IV')
        self.assertEqual(resultado, 4)
    def test_V(self):
        resultado = roman_to_decimal('V')
        self.assertEqual(resultado, 5)
    def test_VI(self):
        resultado = roman_to_decimal('VI')
        self.assertEqual(resultado, 6)
    def test_VII(self):
        resultado = roman_to_decimal('VII')
        self.assertEqual(resultado, 7)
    def test_VIII(self):
        resultado = roman_to_decimal('VIII')
        self.assertEqual(resultado, 8)
    def test_IX(self):
        resultado = roman_to_decimal('IX')
        self.assertEqual(resultado, 9)
    def test_X(self):
        resultado = roman_to_decimal('X')
        self.assertEqual(resultado, 10)

#TEST START
if __name__ == '__main__':
    unittest.main()

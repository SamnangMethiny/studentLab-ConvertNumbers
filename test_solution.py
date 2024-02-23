import unittest
from student_solution import hexToDecimal, decimalToBinary  # Assume student_solution.py is where students write their code

class TestConversions(unittest.TestCase):
    def test_hex_to_decimal(self):
        self.assertEqual(hexToDecimal('A'), 10)
        self.assertEqual(hexToDecimal('1A'), 26)
        self.assertEqual(hexToDecimal('10'), 16)

    def test_decimal_to_binary(self):
        self.assertEqual(decimalToBinary(2), '10')
        self.assertEqual(decimalToBinary(5), '101')
        self.assertEqual(decimalToBinary(10), '1010')

if __name__ == '__main__':
    unittest.main()

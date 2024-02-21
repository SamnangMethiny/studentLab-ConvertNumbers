# test_solution.py

import unittest
from student_solution import binary_to_hex, hex_to_binary

class TestConversion(unittest.TestCase):
    def test_binary_to_hex(self):
        self.assertEqual(binary_to_hex('1010'), 'a')
        self.assertEqual(binary_to_hex('1111'), 'f')
        self.assertEqual(binary_to_hex('10011010010'), '4d2')
    
    def test_hex_to_binary(self):
        self.assertEqual(hex_to_binary('a'), '1010')
        self.assertEqual(hex_to_binary('f'), '1111')
        self.assertEqual(hex_to_binary('4d2'), '10011010010')

if __name__ == '__main__':
    unittest.main()

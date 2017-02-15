import sys
from os import path
sys.path.append(path.join('..'))

from src.acompound_interest import Acompound

import unittest

class TestAcompound(unittest.TestCase):
    '''Tests for Acompound class'''
    def test_calculate_amount(self):
        self.assertEqual(12363.61, Acompound.calculate_amount(12000, 0.01, 3))
        self.assertEqual(5306.04, Acompound.calculate_amount(5000, 0.02, 3))
        self.assertEqual(206.06, Acompound.calculate_amount(200, 0.01, 3))
                                                                                                                
    def test_calculate_capital(self):
        self.assertEqual(505.00, Acompound.calculate_capital(500, 0.01, 1))
        self.assertEqual(510.05, Acompound.calculate_capital(500, 0.01, 2))
        self.assertEqual(12500.00, Acompound.calculate_capital(15237.43, 0.01, 10))
        self.assertEqual(536.07, Acompound.calculate_capital(500, 0.01, 8))
 
    def test_calculate_interest(self):
        self.assertEqual(0.0230, Acompound.calculate_interest(5862.72,5000, 7))
    
    def test_calculate_time_interest(self):
        self.assertEqual(8.00, Acompound.calculate_time_interest(84486.94, 75000, 0.015))

if __name__ == '__main__':
    unittest.main()
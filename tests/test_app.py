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
        self.assertEqual(12000, Acompound.calculate_capital(12363.61, 0.01, 3))
        self.assertEqual(887.45, Acompound.calculate_capital(1000, 0.01, 12))
        
 
    def test_calculate_interest(self):
        self.assertEqual(0.02, Acompound.calculate_interest(5862.72,5000, 7))
    
    def test_calculate_time_interest(self):
        self.assertEqual(8.00, Acompound.calculate_time_interest(84486.94, 75000, 0.015))

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
import unittest
import cf

class ContinuedFractionsTests(unittest.TestCase):
    def test_cf_expansion(self):
        expected = [0, 5, 29, 4, 1, 3, 2, 4, 3] 
        self.assertTrue(cf.cf_expansion(17993, 90581) == expected)
    
    def test_convergents(self):
        cf_expansion = [0, 5, 29, 4, 1, 3, 2, 4, 3] 
        expected = [(0, 1), (1, 5), (29, 146), (117, 589), (146, 735),
                (555, 2794), (1256, 6323), (5579, 28086), (17993, 90581)] 
        self.assertTrue(cf.convergents(cf_expansion))

if __name__ == '__main__':
    unittest.main()

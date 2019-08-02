import unittest
import codingtest

class TestCalc(unittest.TestCase):
    
    def test_take_sum(self):
        result = codingtest.take_sum([10,10,4,4])
        self.assertEqual(result, 28)
        
    def test_take_average(self):
        result = codingtest.take_average([10,10,4,4])
        self.assertEqual(result, 7)
        
    def test_take_median(self):
        result = codingtest.take_median([4,4,2,2,6,6])
        self.assertEqual(result, 4)
        
    def test_calculate_operation_1(self):
        result = codingtest.calculate_operation([10,10,4,4], 'avg')
        self.assertEqual(result, 7)
        
    def test_calculate_operation_2(self):
        result = codingtest.calculate_operation([10,10,4,4], 'sum')
        self.assertEqual(result, 28)
        
    def test_calculate_operation_3(self):
        result = codingtest.calculate_operation([4,4,2,2,6,6], 'median')
        self.assertEqual(result, 4)
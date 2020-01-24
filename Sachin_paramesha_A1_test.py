import unittest
from Sachin_paramesha_A1 import classify_triangle

class TestClassifyTriangle(unittest.TestCase):

    def test_classify_triangle(self):
        
        self.assertEqual(classify_triangle(8, 8, 8), 'Equilateral triangle')
        self.assertNotEqual(classify_triangle(4, 2, 5), 'Equilateral triangle')

        self.assertEqual(classify_triangle(-1, 0, 5), 'Not a triangle')
        self.assertEqual(classify_triangle(1.2, 0, 1), 'Not a triangle')
        self.assertEqual(classify_triangle('a', 0, 1), 'Not a triangle')

        self.assertEqual(classify_triangle(3, 4, 5), 'Right angle triangle')
        self.assertEqual(classify_triangle(6, 8, 10), 'Right angle triangle')

        self.assertEqual(classify_triangle(4, 4, 6), 'Isosceles triangle')
        self.assertNotEqual(classify_triangle(1, 3, 5), 'Isosceles triangle')

        self.assertEqual(classify_triangle(4, 5, 6), 'Scalene triangle')
        self.assertEqual(classify_triangle(1.1, 2, 3), 'Scalene triangle')

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

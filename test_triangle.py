# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Sachin Paramesha
"""

import unittest

from triangle_123 import classify_triangle

# This code implside_ameside_btsside_cthe unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    """define multiple sets of tests as functions with names that begin"""

    def test_valid_input(self):
        """T1: To Verify the Valid Input"""
        self.assertEqual(classify_triangle(2, 2, -3), "InvalidInput")
        self.assertEqual(classify_triangle(2.3, 2.1, 3), "InvalidInput")

    def test_equilateral_triangles(self):
        """T2: If the sides are all equal, then the triangle is “Equilateral” """
        self.assertEqual(
            classify_triangle(1, 1, 1), "Equilateral", "1,1,1 should be equilateral"
        )
        self.assertEqual(
            classify_triangle(6, 6, 6), "Equilateral", "6,6,6 should be equilateral"
        )

    def test_right_triangle_a(self):
        """T3: To determine if the triangle is a "Right" angle triangle or not"""
        self.assertEqual(
            classify_triangle(3, 4, 5), "Right", "3,4,5 is a Right triangle"
        )
        self.assertEqual(
            classify_triangle(8, 6, 10), "Right", "8,6,10 is a Right triangle"
        )
        self.assertEqual(
            classify_triangle(20, 15, 25), "Right", "20,15,25 is a Right triangle"
        )

    def test_right_triangle_b(self):
        """ T4: To determine if the triangle is a "Right" angle triangle or not """
        self.assertEqual(
            classify_triangle(5, 3, 4), "Right", "5,3,4 is a Right triangle"
        )
        self.assertEqual(
            classify_triangle(10, 6, 8), "Right", "10,6,8 is a Right triangle"
        )

    def test_scalene_triangles(self):
        """ T5: If all the three sides of the traingle ar not equal,
        then the triangle is "Scalene" """
        self.assertEqual(
            classify_triangle(2, 4, 5), "Scalene", "2,4,5 should be Scalene"
        )
        self.assertEqual(
            classify_triangle(100, 101, 102), "Scalene", "100,101,102 should be Scalene"
        )

    def test_isoceles_triangles(self):
        """ T6: if two sides are equal, but not three side, then the triangle is “Isosceles” """
        self.assertEqual(
            classify_triangle(2, 5, 5), "Isosceles", "2,4,5 should be Isoceles"
        )
        self.assertEqual(
            classify_triangle(6, 6, 7), "Isosceles", "6,101,102 should be Isoceles"
        )


if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
    
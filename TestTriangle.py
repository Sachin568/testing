# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Sachin Paramesha
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidInput(self):
        """
        To Verify the Valid Input
        """
        self.assertEqual(classifyTriangle(2, 2, -3), 'InvalidInput')
        self.assertEqual(classifyTriangle(2.3, 2.1, 3), 'InvalidInput')

    def testEquilateralTriangles(self): 
        """
        If the sides are all equal, then the triangle is “Equilateral”
        """
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(6,6,6),'Equilateral','6,6,6 should be equilateral')
    

    def testRightTriangleA(self): 
        """
        To determine if the triangle is a "Right" angle triangle or not
        """
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(8,6,10),'Right','8,6,10 is a Right triangle')
        self.assertEqual(classifyTriangle(20,15,25),'Right','20,15,25 is a Right triangle')

    def testRightTriangleB(self):
        """
        To determine if the triangle is a "Right" angle triangle or not
        """ 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertEqual(classifyTriangle(10,6,8),'Right','10,6,8 is a Right triangle')
        
    def testScaleneTriangles(self):
        """
        If all the three sides of the traingle ar not equal, then the triangle is "Scalene"
        """ 
        self.assertEqual(classifyTriangle(2,4,5),'Scalene','2,4,5 should be Scalene')
        self.assertEqual(classifyTriangle(100,101,102),'Scalene','100,101,102 should be Scalene')

    def testIsocelesTriangles(self):
        """
        if two sides are equal, but not three side, then the triangle is “Isosceles”
        """
        self.assertEqual(classifyTriangle(2,5,5),'Isoceles','2,4,5 should be Isoceles')
        self.assertEqual(classifyTriangle(6,6,7),'Isoceles','6,101,102 should be Isoceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


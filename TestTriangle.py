"""@author: Xiaoyu Li
Created on 1/28/2018
A set of test cases for classifying triangle
"""

import unittest
from Triangle import classifyTriangle

class TestTriangle(unittest.TestCase):
    def test_invalid1(self):
        self.assertEqual(classifyTriangle(200, 201, 50),'InvalidInput')
    def test_invalid2(self):
        self.assertEqual(classifyTriangle(0, 5, 5), 'InvalidInput')
        self.assertEqual(classifyTriangle(10.5, 5, 5), 'InvalidInput')
    def test_invalid3(self):
        self.assertEqual(classifyTriangle(-5, 5.5, 5), 'InvalidInput')
    def test_invalid4(self):
        self.assertNotEqual(classifyTriangle(200, 200, 200), 'InvalidInput')
    
    def test_etriangle1(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
    def test_etriangle2(self):
        self.assertNotEqual(classifyTriangle(2,2,3),'Equilateral')
    def test_etriangle3(self):
        self.assertNotEqual(classifyTriangle(0,0,0),'Equilateral')
    
    def test_not_a_triangle1(self):
        self.assertEqual(classifyTriangle(2,1,1),'NotATriangle')
    def test_not_a_triangle2(self):
        self.assertEqual(classifyTriangle(1,2,1),'NotATriangle')
    def test_not_a_triangle3(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle')
    def test_not_a_triangle4(self):
        self.assertEqual(classifyTriangle(200,190,9),'NotATriangle')
    def test_not_a_triangle5(self):
        self.assertNotEqual(classifyTriangle(5,3,4),'NotATriangle')
    def test_not_a_triangle6(self):
        self.assertNotEqual(classifyTriangle(200,190,11),'NotATriangle')

    def test_isosceles_triangle1(self):
        self.assertEqual(classifyTriangle(2,2,3),'Isosceles')
    def test_isosceles_triangle2(self):
        self.assertNotEqual(classifyTriangle(2,2,2),'Isosceles')
    def test_isosceles_triangle3(self):
        self.assertNotEqual(classifyTriangle(2,2,10),'Isosceles')
    def test_isosceles_triangle4(self):
        self.assertNotEqual(classifyTriangle(-1,-1,2),'Isosceles')
    def test_isosceles_triangle5(self):
        self.assertEqual(classifyTriangle(2,3,3),'Isosceles')

    def test_Scalene_triangle1(self):
        self.assertEqual(classifyTriangle(6,4,3),'Scalene')
    def test_Scalene_triangle2(self):
        self.assertNotEqual(classifyTriangle(6,4,4),'Scalene')

    def test_right_triangle1(self):
        self.assertEqual(classifyTriangle(5,4,3),'Right')
    def test_right_triangle2(self):
        self.assertEqual(classifyTriangle(4,5,3),'Right')
    def test_right_triangle3(self):
        self.assertEqual(classifyTriangle(6,8,10),'Right')

if __name__ == '__main__':
    unittest.main()

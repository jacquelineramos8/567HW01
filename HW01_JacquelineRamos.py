"""
    Author: Jacqueline Ramos
    Assignment: HW01
    Description: The code below receives triangle side input using the if __name__ == '__main__' function and classifies that triangle as:
    equilateral, isosceles, scalene, right, or not a triangle. I left the code intentionally with bugs to demonstrate how
    proper unit testing can catch these bugs. 
"""
import unittest

def classify_triangle(a, b, c):
    """ This function is meant to classify the triangle by its side lengths a, b, c and return that classification.
        The triangle can be equilateral (all sides equal),
        isosceles (two sides equal),
        right (a^2 + b^2 = c^2),
        scalene (all sides different lengths,
        or not a triangle. """
    
    if a == b and a == c:
        return 'Equilateral Triangle'
    elif a == b or b == c or c == a:
        return 'Isosceles Triangle'
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right Triangle'
    elif (a + b <= c) or (b + c <= a) or (a + c <= b):
        return 'Not a triangle!'
    else:
        return 'Scalene Triangle'

def run_classification(a, b, c):
    """ This function prints the triangle classification. """
    print('Triangle (',a,',',b,',',c,') classification:',classify_triangle(a,b,c))




class TestTriangles(unittest.TestCase):
    """ This class holds the test cases for the classify_triangle function. """

    def test_set1(self) -> None:
        """ This first test set deomonstrates that appropriate side length inputs are classified correctly. """
        self.assertEqual(classify_triangle(3,3,3), 'Equilateral Triangle')
        self.assertEqual(classify_triangle(3,3,5), 'Isosceles Triangle')
        self.assertEqual(classify_triangle(3,4,5), 'Right Triangle')
        self.assertEqual(classify_triangle(3,5,7), 'Scalene Triangle')
        self.assertEqual(classify_triangle(3,5,8), 'Not a triangle!')
    
    def test_set2(self) -> None:
        """ This test set ensures that triangles aren't accidentally labeled as isosceles or
            that isosceles triangles aren't accidentally labeled as scalene """ 
        self.assertNotEqual(classify_triangle(9,9,9), 'Isosceles Triangle')
        self.assertNotEqual(classify_triangle(3,9,9), 'Scalene Triangle')
        self.assertNotEqual(classify_triangle(9,3,9), 'Scalene Triangle')
        
    def test_set3(self) -> None:
        """ This test set is to see if right triangle side lengths input in various orders are still labeled as right triangles.
            This test set should fail because my code classifies right triangles only as a^2 + b^2 = c^2 and does not take into account
            the hypotenuse side being input as side a or b """
        self.assertEqual(classify_triangle(5,4,3), 'Right Triangle') # the buggy code will label this triangle as scalene
    
    def test_set4(self) -> None:
        """ This test set tests invalid side lengths like 0 or negative numbers. 
            These tests should also fail because my code did not safeguard against invalid inputs with a try/except block """
        self.assertEqual(classify_triangle(0,0,0), 'Not a triangle!') # the buggy code will label this triangle as equilateral
        self.assertEqual(classify_triangle(-3,4,5), 'Not a triangle!') # the buggy code will label this triangle as right


if __name__ == '__main__':
    """ Below I just print out some of the triangle classifications that I will be testing """
    run_classification(3,3,3)
    run_classification(3,3,5)
    run_classification(3,4,5)
    run_classification(3,5,7)
    run_classification(3,5,8)

    """ Below the unittest functions are called """
    unittest.main(exit=False)




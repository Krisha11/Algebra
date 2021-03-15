import unittest
from Test import *
from Matrix import Matrix
from Vector import Vector
from lib import zerosGaussSeidel, GaussSeidel, checkGaussSeidel, BAD_INPUT_GAUSS_SEIDEL_MSG


class TestGaussSeidel(unittest.TestCase):

    def test_inOne(self):
        self.assertFalse(zerosGaussSeidel(m1))
        self.assertFalse(zerosGaussSeidel(m2))
        self.assertTrue(zerosGaussSeidel(m3))
        self.assertFalse(zerosGaussSeidel(e1))
        self.assertFalse(zerosGaussSeidel(e2))
        self.assertFalse(zerosGaussSeidel(e1000))

    def test_bad_input(self):
        self.assertEqual(GaussSeidel(3, m3, v3_1, 1),
                         BAD_INPUT_GAUSS_SEIDEL_MSG)

    def test_algo(self):
        e = 0.1
        self.assertTrue(checkGaussSeidel(
            GaussSeidel(1, e1, v1_1, e), e1, v1_1, e))
        self.assertTrue(checkGaussSeidel(
            GaussSeidel(2, e2, v2_1, e), e2, v2_1, e))
        self.assertTrue(checkGaussSeidel(
            GaussSeidel(2, e2, v2_2, e), e2, v2_2, e))
        self.assertTrue(checkGaussSeidel(
            GaussSeidel(3, m1, v3_1, e), m1, v3_1, e))
        self.assertTrue(checkGaussSeidel(
            GaussSeidel(3, m1, v3_2, e), m1, v3_2, e))
        self.assertTrue(checkGaussSeidel(
            GaussSeidel(1, e1, v1_2, e), e1, v1_2, e))
        self.assertTrue(checkGaussSeidel(
            GaussSeidel(2, e2, v2_3, e), e2, v2_3, e))


if __name__ == "__main__":
    unittest.main()

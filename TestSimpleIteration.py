import unittest
from Test import *
from Matrix import Matrix
from Vector import Vector
from lib import inOneSimpleIter, simpleIter, checkSimpleIter, BAD_INPUT_SIMPLE_ITER_MSG, CODE_LOOPED_MSG


class TestSimpleIteration(unittest.TestCase):
    def test_inOne(self):
        self.assertTrue(inOneSimpleIter(m1))
        self.assertFalse(inOneSimpleIter(m2))
        self.assertTrue(inOneSimpleIter(e1))
        self.assertTrue(inOneSimpleIter(e2))
        self.assertTrue(inOneSimpleIter(e1000))

    def test_bad_input(self):
        self.assertEqual(simpleIter(3, m2, v3_1, 1), BAD_INPUT_SIMPLE_ITER_MSG)

    def test_looped(self):
        self.assertEqual(simpleIter(1, e1, v1_1, 1), CODE_LOOPED_MSG)
        self.assertEqual(simpleIter(2, e2, v2_1, 1), CODE_LOOPED_MSG)
        self.assertEqual(simpleIter(2, e2, v2_2, 0.1), CODE_LOOPED_MSG)

    def test_big_e(self):
        self.assertTrue(checkSimpleIter(
            simpleIter(2, e2, v2_2, 1), e2, v2_2, 1))

    def test_small_e(self):
        e = 0.1
        self.assertTrue(checkSimpleIter(
            simpleIter(3, m1, v3_1, e), m1, v3_1, e))
        self.assertTrue(checkSimpleIter(
            simpleIter(3, m1, v3_2, e), m1, v3_2, e))
        self.assertTrue(checkSimpleIter(
            simpleIter(1, e1, v1_2, e), e1, v1_2, e))
        self.assertTrue(checkSimpleIter(
            simpleIter(2, e2, v2_3, e), e2, v2_3, e))
        self.assertTrue(checkSimpleIter(simpleIter(
            1000, e1000, v1000, e), e1000, v1000, e))


if __name__ == "__main__":
    unittest.main()

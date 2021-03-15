import unittest
from Test import *
from Matrix import Matrix
from Vector import Vector
from lib import getLamQRSimpleIter, QRSimpleIter, getErrorQRSimpleIter


class TestQRSimpleIteration(unittest.TestCase):
    def test_getLam(self):
        self.assertEqual(getLamQRSimpleIter(e1, v1_1.normalize()), 1)
        self.assertEqual(getLamQRSimpleIter(e1, v1_2.normalize()), 0)
        self.assertEqual(getLamQRSimpleIter(e2, v2_1.normalize()), 1)
        self.assertEqual(getLamQRSimpleIter(e2, v2_2.normalize()), 1)
        self.assertEqual(getLamQRSimpleIter(e2, v2_3.normalize()), 1)
        self.assertEqual(getLamQRSimpleIter(e1000, v1000.normalize()), 0)

    def test_algo(self):
        l = [m1, m2, m3, e1, e2, e1000]
        e = [1, 0.1, 0.01]
        for i in range(len(l)):
            for q in range(len(e)):
                a = Matrix([[l[i].a[k][j] for j in range(l[i].n)]
                            for k in range(l[i].n)])
                x = Vector([1 if j == 0 else 0 for j in range(l[i].n)])

                v = QRSimpleIter(a, x, e[q])
                lam = getLamQRSimpleIter(a, v)

                self.assertTrue(getErrorQRSimpleIter(a, v) < e[q])
                self.assertTrue((a.mulVector(v) - v.mulConst(lam)).norm() < e[q])


if __name__ == "__main__":
    unittest.main()

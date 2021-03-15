import unittest
from Test import *
from Matrix import Matrix
from Vector import Vector
from lib import maxGershgorianRQRAlgo, QRAlgo


class TestQRAlgo(unittest.TestCase):
    def test_maxGershgorianRQRAlgo(self):
        self.assertEqual(maxGershgorianRQRAlgo(e1), 0)
        self.assertEqual(maxGershgorianRQRAlgo(e2), 0)
        self.assertEqual(maxGershgorianRQRAlgo(m2), 6)

    def test_algo(self):
        l = [m1, m2, m3, e1, e2]
        e = [1, 0.1, 0.01]
        for i in range(len(l)):
            for j in range(len(e)):
                a = Matrix([[l[i].a[k][n] for n in range(l[i].n)]
                            for k in range(l[i].n)])

                qk, ak = QRAlgo(a, e[j])

                self.assertTrue(qk.n == ak.n == l[i].n)
                self.assertTrue(qk.is_orthogonal()
                                and maxGershgorianRQRAlgo(ak) < e[j])
                self.assertTrue(l[i] == qk.mulMatrix(ak).mulMatrix(qk.transpose()))


if __name__ == "__main__":
    unittest.main()

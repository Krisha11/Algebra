import unittest
from Test import *
from Matrix import Matrix
from Vector import Vector
from lib import QRHausholder, stepQRHausholder


class TestQRHausholder(unittest.TestCase):
    def test_step(self):
        l = [m1, m2, m3, e1, e2]
        for i in range(len(l)):
            q = Matrix([[(float)(1 if k == j else 0)
                         for j in range(l[i].n)] for k in range(l[i].n)])
            a = Matrix([[l[i].a[k][j] for j in range(l[i].n)]
                        for k in range(l[i].n)])
            for t in range(l[i].n):
                q, a = stepQRHausholder(t, q, a)

                self.assertTrue(q.is_orthogonal() and a.get_k_main_minor(
                    t + 1).is_uppertriangular())
                self.assertTrue(l[i].get_k_main_minor(
                    t + 1) == q.transpose().mulMatrix(a).get_k_main_minor(t + 1))

    def test_algo(self):
        l = [m1, m2, m3, e1, e2]
        for i in range(len(l)):
            q, r = QRHausholder(
                Matrix([[l[i].a[k][j] for j in range(l[i].n)] for k in range(l[i].n)]))
            self.assertTrue(q.n == r.n == l[i].n)
            self.assertTrue(q.is_orthogonal() and r.is_uppertriangular())
            self.assertTrue(l[i] == q.mulMatrix(r))


if __name__ == "__main__":
    unittest.main()

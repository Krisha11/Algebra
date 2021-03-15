import unittest
from Test import *
from Matrix import Matrix
from Vector import Vector
from lib import stepThreeDiagAlgo, threeDiagAlgo


def is_first_k_tridiag(a, k):
    for i in range(a.n):
        for j in range(a.n):
            if not (i == j or i == j + 1 or i == j - 1 or i >= k and j >= k) and math.fabs(a.a[i][j]) > Matrix.e:
                return False
    return True


class TestTridiag(unittest.TestCase):
    def test_step(self):
        l = [m1, m2, m3, e1, e2]
        for i in range(len(l)):
            a = Matrix([[l[i].a[k][j] for j in range(l[i].n)]
                        for k in range(l[i].n)])
            q = Matrix([[(1 if k == j else 0) for j in range(a.n)]
                        for k in range(a.n)])
            for j in range(a.n - 2):
                q, a = stepThreeDiagAlgo(a, q, j)

                self.assertTrue(q.n == a.n == l[i].n)
                self.assertTrue(q.is_orthogonal() and is_first_k_tridiag(a, j))
                self.assertTrue(l[i] == q.mulMatrix(a).mulMatrix(q.transpose()))

    def test_algo(self):
        l = [m1, m2, m3, e1, e2]
        for i in range(len(l)):
            q, a = threeDiagAlgo(l[i])

            self.assertTrue(q.n == a.n == l[i].n)
            self.assertTrue(q.is_orthogonal() and a.is_tridiag())
            self.assertTrue(l[i] == q.mulMatrix(a).mulMatrix(q.transpose()))


if __name__ == "__main__":
    unittest.main()

import math
import lib
import Vector


class Matrix:
    e = 1e-2

    def __init__(self, arr):
        self.a = arr
        self.n = len(self.a)

    def __neg__(self):
        return Matrix([[-self.a[i][j] for j in range(self.n)] for i in range(self.n)])

    def transpose(self):
        return Matrix([[self.a[j][i] for j in range(self.n)] for i in range(self.n)])

    def printMatrix(self):
        for i in range(self.n):
            for j in range(self.n):
                print(round(self.a[i][j], 8), end=' ')
            print()

    def givensRotation(self, i, j, c, s):
        u_new = [c * self.a[i][q] + s * self.a[j][q] for q in range(self.n)]
        v_new = [-s * self.a[i][q] + c * self.a[j][q] for q in range(self.n)]
        self.a[i], self.a[j] = u_new, v_new

    def __eq__(self, other):
        if self.n != other.n:
            return False

        for i in range(self.n):
            for j in range(self.n):
                if math.fabs(self.a[i][j] - other.a[i][j]) > Matrix.e:
                    return False
        return True

    def mulVector(self, t):
        res = Vector.Vector([0 for i in range(self.n)])
        for i in range(self.n):
            for j in range(self.n):
                res.a[i] = res.a[i] + self.a[i][j] * t.a[j]
        return res

    def mulMatrix(self, t):
        res = Matrix([[0 for j in range(self.n)] for i in range(self.n)])
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    res.a[i][j] = res.a[i][j] + self.a[i][k] * t.a[k][j]
        return res

    def is_e(self):
        if not self.is_diagonal():
            return False
        for i in range(self.n):
            for j in range(self.n):
                if i == j and math.fabs(self.a[i][j] - 1) > Matrix.e :
                    return False
        return True

    def is_diagonal(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and math.fabs(self.a[i][j]) > Matrix.e:
                    return False
        return True

    def is_orthogonal(self):
        return self.mulMatrix(self.transpose()).is_e()

    def is_uppertriangular(self):
        for i in range(self.n):
            for j in range(self.n):
                if i > j and math.fabs(self.a[i][j]) > Matrix.e:
                    return False
        return True

    def is_tridiag(self):
        for i in range(self.n):
            for j in range(self.n):
                if not (i == j or i == j + 1 or i == j - 1) and math.fabs(self.a[i][j]) > Matrix.e:
                    return False
        return True

    def is_simmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.a[i][j] != self.a[j][i]:
                    return False
        return True

    def get_k_main_minor(self, k):
        sz = min(self.n, k)
        return Matrix([[self.a[i][j] for j in range(sz)] for i in range(sz)])

    # обращение матрицы
    def getInverse(self):
        c = Matrix([[self.a[i][j] for j in range(self.n)]
                    for i in range(self.n)])
        res = Matrix([[(1 if i == j else 0) for j in range(self.n)]
                      for i in range(self.n)])
        for i in range(self.n):
            if c.a[i][i] == 0:
                return Matrix([])
            d = c.a[i][i]
            c.a[i][i] /= d
            for j in range(self.n):
                res.a[i][j] /= d

            for t in range(i + 1, self.n):
                d = c.a[t][i]
                c.a[t][i] -= d
                for j in range(self.n):
                    res.a[t][j] -= d * res.a[i][j]
        return res

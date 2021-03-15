import math
import lib
import Matrix


class Vector:
    e = 1e-2

    def __init__(self, arr):
        self.a = arr
        self.n = len(self.a)

    def __sub__(self, other):
        return Vector([self.a[i] - other.a[i] for i in range(self.n)])

    def __add__(self, other):
        return Vector([self.a[i] + other.a[i] for i in range(self.n)])

    def __str__(self):
        return str(self.a)

    def norm(self):
        return math.fsum([math.fabs(self.a[i]) for i in range(self.n)])

    def __eq__(self, other):
        if self.n != other.n:
            return False

        for i in range(self.n):
            if math.fabs(self.a[i] - other.a[i]) > Vector.e:
                return False
        return True

    def hausholderMul(self, a):
        vtat = Vector([0 for _ in range(a.n)])
        for i in range(a.n):
            for k in range(a.n):
                vtat.a[i] += self.a[k] * a.a[k][i]

        vvta = Matrix.Matrix([[self.a[i] * vtat.a[j]
                               for j in range(a.n)] for i in range(a.n)])
        return Matrix.Matrix([[(a.a[i][j] - 2 * vvta.a[i][j]) for j in range(a.n)] for i in range(a.n)])

    def norm(self):
        return math.sqrt(math.fsum([self.a[i] * self.a[i] for i in range(self.n)]))

    def printVector(self):
        for i in range(self.n):
            print(round(self.a[i], 6), end=' ')
        print()

    def mulMatrix(self, t):
        ans = Vector([0 for _ in range(t.n)])
        for i in range(t.n):
            for k in range(t.n):
                ans.a[i] += self.a[k] * t.a[k][i]

        return ans

    def mulVector(self, t):
        return Matrix.Matrix([[self.a[i] * t.a[j] for j in range(t.n)] for i in range(t.n)])

    def mulConst(self, c):
        return Vector([self.a[i] * c for i in range(self.n)])

    def hausholderMulQ(self, a):
        vtat = self.mulMatrix(a)
        vvta = self.mulVector(vtat)
        return Matrix.Matrix([[(a.a[i][j] - 2 * vvta.a[i][j]) for j in range(a.n)] for i in range(a.n)])

    def hausholderMulA(self, a):
        a1 = self.hausholderMulQ(a)

        vtat = self.mulMatrix(a)
        vvta = self.mulVector(vtat)

        av = a.mulVector(self)
        avvt = av.mulVector(self)

        vtavvt = self.mulMatrix(avvt)
        vvtavvt = self.mulVector(vtavvt)

        return Matrix.Matrix([[(a.a[i][j] - 2 * vvta.a[i][j] - 2 * avvt.a[i][j] + 4 * vvtavvt.a[i][j]) for j in range(a.n)] for i in range(a.n)])

    def normalize(self):
        n = self.norm()
        if n == 0:
            n = 1
        return Vector([self.a[i] / n for i in range(self.n)])

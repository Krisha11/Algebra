import math
import Matrix
import Vector

CODE_LOOPED_MSG = "Sorry.. Code looped."
BAD_INPUT_GAUSS_SEIDEL_MSG = "Bad input. The diagonal of the matrix A contains zeros . \n"
BAD_INPUT_SIMPLE_ITER_MSG = "Bad input. Gershgorin circles do not lie in the unit circle centered at zero. \n"
MAX_STEPS = 100000
MAX_BAD_STEPS = 20


# -----------------------------------------------------------------------------------------------------------------------------
# Метод простой итерации
# x = Ax + b с погрешностью по норме не более e. A - квадратная, x - ?


def checkSimpleIter(x, a, b, e):
    return (x - a.mulVector(x) - b).norm() < e


def stepSimpleIter(x, a, b):
    x_new = a.mulVector(x) + b
    return x_new


def inOneSimpleIter(a):
    for i in range(a.n):
        r = math.fsum([math.fabs(a.a[i][j]) for j in range(a.n) if i != j])
        if a.a[i][i] + r > 1 or a.a[i][i] - r < -1:
            return False
    return True


def simpleIter(n, a, b, e):
    x = Vector.Vector([0 for _ in range(n)])
    inOne = inOneSimpleIter(a)
    if not inOne:
        return BAD_INPUT_SIMPLE_ITER_MSG

    bad_steps = 0
    steps = 0
    while (not checkSimpleIter(x, a, b, e)
           and bad_steps < MAX_BAD_STEPS
           and steps < MAX_STEPS):
        x_new = stepSimpleIter(x, a, b)

        delta = x_new.norm() - x.norm()
        bad_steps = (bad_steps + 1) if (delta >= 1) else 0
        x = x_new
        steps += 1

    if (bad_steps == MAX_BAD_STEPS
            or steps == MAX_STEPS):
        return CODE_LOOPED_MSG
    return x

# -----------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------
# Метод Гаусса-Зейделя
# Ax = b с погрешностью по норме не более e. A - квадратная, x - ?


def checkGaussSeidel(x, a, b, e):
    return (a.mulVector(x) - b).norm() < e


def stepGaussSeidel(x, u, ml, b):
    x = ml.mulVector(((-u).mulVector(x) + b))
    return x


def zerosGaussSeidel(a):
    for i in range(a.n):
        if a.a[i][i] == 0:
            return True
    return False


def GaussSeidel(n, a, b, e):
    ml = a.getInverse()
    u = Matrix.Matrix([[(a.a[i][j] if i < j else 0)
                        for j in range(a.n)] for i in range(a.n)])

    x = Vector.Vector([0 for _ in range(n)])
    withZeros = zerosGaussSeidel(a)
    if withZeros:
        return BAD_INPUT_GAUSS_SEIDEL_MSG

    bad_steps = 0
    steps = 0
    while (not checkGaussSeidel(x, a, b, e)
           and bad_steps < MAX_BAD_STEPS
           and steps < MAX_STEPS):
        x_new = stepGaussSeidel(x, u, ml, b)
        delta = x_new.norm() - x.norm()
        if delta >= 1:
            bad_steps = bad_steps + 1
        else:
            bad_steps = 0
        x = x_new
        steps = steps + 1

    if (bad_steps == MAX_BAD_STEPS
            or steps == MAX_STEPS):
        return CODE_LOOPED_MSG
    return x

# -----------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------
# QR-разложение при помощи вращений Гивенса за O(n^3)
# A = QR, Q - унитарная(ортогональная), R - верхнетреугольная; Q,R - ?


def firstNotZeroQRGivens(i, a):
    for j in range(i, a.n):
        if a.a[j][i] != 0:
            return j
    return -1


def killQRGivens(j, id, i, q, a):
    x_id = a.a[id][i]
    x_j = a.a[j][i]
    c = x_id / math.sqrt(x_id * x_id + x_j * x_j)
    s = x_j / math.sqrt(x_id * x_id + x_j * x_j)
    q.givensRotation(id, j, c, s)
    a.givensRotation(id, j, c, s)

    return q, a


def stepQRGivens(i, q, a):
    # find not zero element
    id = firstNotZeroQRGivens(i, a)
    if id == -1:
        return q, a

    # kill others
    for j in range(id + 1, a.n):
        q, a = killQRGivens(j, id, i, q, a)

    # put on diag
    if id != i:
        x_i = a.a[i][i]
        x_id = a.a[id][i]
        c = x_i / (x_i * x_i + x_id * x_id)
        s = x_id / (x_i * x_i + x_id * x_id)
        q.givensRotation(i, id, c, s)
        a.givensRotation(i, id, c, s)

    return q, a


def QRGivens(a):
    q = Matrix.Matrix([[(float)(1 if i == j else 0)
                        for i in range(a.n)] for j in range(a.n)])
    for i in range(a.n):
        q, a = stepQRGivens(i, q, a)

    return q.transpose(), a

# -----------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------
# QR-разложение при помощи отражений Хаусхолдера за O(n^3)
# A = QR, Q - унитарная(ортогональная), R - верхнетреугольная; Q,R - ?


def stepQRHausholder(i, q, a):
    v = Vector.Vector([a.a[j + i][i] for j in range(a.n - i)])
    normV = v.norm()
    if normV == 0:
        return q, a

    u = Vector.Vector([v.a[j] / normV for j in range(a.n - i)])

    ume1 = u
    ume1.a[0] = ume1.a[0] - 1
    normUme1 = ume1.norm()
    if normUme1 == 0:
        return q, a

    res_u = Vector.Vector([ume1.a[j] / normUme1 for j in range(a.n - i)])

    u_n = Vector.Vector([(0 if j < i else res_u.a[j - i]) for j in range(a.n)])

    resQ = u_n.hausholderMul(q)
    resA = u_n.hausholderMul(a)

    return resQ, resA


def QRHausholder(a):
    q = Matrix.Matrix([[(float)(1 if i == j else 0)
                        for i in range(a.n)] for j in range(a.n)])
    for i in range(a.n):
        q, a = stepQRHausholder(i, q, a)

    return q.transpose(), a

# -----------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------
# Приближенное нахождение максимального собственного числа и соответствующего
# собственного вектора методом простой итерации.
# Матрица A, x_0 e, ||Av - lv|| < e, v, l - ?


def stepQRSimpleIter(a, x):
    v = a.mulVector(x)
    c = 1 / v.norm()
    return Vector.Vector([c * v.a[i] for i in range(v.n)])


def getLamQRSimpleIter(a, v):
    av = a.mulVector(v)
    lam = 0
    for i in range(a.n):
        lam = lam + v.a[i] * av.a[i]
    return lam


def getErrorQRSimpleIter(a, v):
    av = a.mulVector(v)
    lam = getLamQRSimpleIter(a, v)
    avlv = Vector.Vector([av.a[i] - lam * v.a[i] for i in range(v.n)])
    return avlv.norm()


def QRSimpleIter(a, v, e):
    iters = 0
    max_iters = 10000
    while getErrorQRSimpleIter(a, v) > e and iters < max_iters:
        v = stepQRSimpleIter(a, v)
        iters = iters + 1

    if iters == max_iters:
        return CODE_LOOPED_MSG
    return v

# -----------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------
# Приближенное нахождение спектра симметричной матрицы.(QR алгоритм)
# Симметричная матрица A, e. A_k и матрица Q^{(k)}, для такого k,
# что радиусы кругов Гершгорина у A_k меньше \epsilon.
# A = Q^{(k)} \cdot A_k Q^{(k)^T}?


def maxGershgorianRQRAlgo(a):
    return max([math.fsum([math.fabs(a.a[i][j]) for j in range(a.n)]) - math.fabs(a.a[i][i]) for i in range(a.n)])


def stepQRAlgo(a):
    q, r = QRHausholder(a)
    return q, r.mulMatrix(q)


def QRAlgo(a, e):
    res = Matrix.Matrix([[(1 if i == j else 0)
                          for j in range(a.n)] for i in range(a.n)])
    steps = 0
    while maxGershgorianRQRAlgo(a) > e and steps < MAX_STEPS:
        q, a = stepQRAlgo(a)
        res = res.mulMatrix(q)

    if steps == MAX_STEPS:
        return CODE_LOOPED_MSG
    return res, a

# -----------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------
# Нахождение тридиагонализации матрицы за O(n^3).
# Симметричная матрица A, e. A' – тридиагонализация матрицы A,
# ортогональная матрица Q, что Q^T \cdot A \cdot Q = A'

def stepThreeDiagAlgo(a, q, i):
    v = Vector.Vector([a.a[j + i + 1][i] for j in range(a.n - i - 1)])
    normV = v.norm()
    if normV == 0:
        return q, a

    u = Vector.Vector([v.a[j] / normV for j in range(a.n - i - 1)])

    ume1 = u
    ume1.a[0] = ume1.a[0] - 1
    normUme1 = ume1.norm()
    if normUme1 == 0:
        return q, a

    res_u = Vector.Vector([ume1.a[j] / normUme1 for j in range(a.n - i - 1)])

    u_n = Vector.Vector([(0 if j <= i else res_u.a[j - i - 1])
                         for j in range(a.n)])

    resQ = u_n.hausholderMulQ(q)
    resA = u_n.hausholderMulA(a)

    return resQ, resA


def threeDiagAlgo(a):
    q = Matrix.Matrix([[(1 if k == j else 0)
                        for j in range(a.n)] for k in range(a.n)])
    for i in range(a.n - 2):
        q, a = stepThreeDiagAlgo(a, q, i)

    return q, a

# -----------------------------------------------------------------------------------------------------------------------------

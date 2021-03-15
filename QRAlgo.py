from Matrix import Matrix
from Vector import Vector
from lib import QRAlgo


def readData():
    print("Введите число n:")
    n = int(input())

    print("Введите матрицу - n строк по n чисел:")
    a = [list(map(float, input().split(' '))) for i in range(n)]

    e = 0.01

    return n, Matrix(a), e


def main():
    n, a, e = readData()

    if not a.is_simmetric():
        print("Реализовано только для симметричных матриц :(")
        return

    res = QRAlgo(a, e)
    if isinstance(res, str):
        print()
        return

    qk, ak = res
    print("Спектр: (почти)")
    for i in range(n):
        print(ak.a[i][i], sep=' ')


if __name__ == "__main__":
    main()

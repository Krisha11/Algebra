from Matrix import Matrix
from Vector import Vector
from lib import QRSimpleIter, getLamQRSimpleIter


def readData():
    print("Введите число n:")
    n = int(input())

    print("Введите матрицу - n строк по n чисел:")
    a = [list(map(float, input().split(' '))) for i in range(n)]

    v = [(1 if i == 0 else 0) for i in range(n)]

    print("Введите точность:")
    e = float(input())

    return n, Matrix(a), Vector(v), e


def main():
    n, a, x, e = readData()
    v = QRSimpleIter(a, x, e)

    lam = getLamQRSimpleIter(a, v)

    if isinstance(lam, str):
        print("Sorry, we don't know how to solve this yet...")
    else:
        print("Почти собственное число:")
        print(lam)
        print("Почти собственный вектор:")
        v.printVector()


if __name__ == "__main__":
    main()

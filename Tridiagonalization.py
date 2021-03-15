from Matrix import Matrix
from Vector import Vector
from lib import threeDiagAlgo


def readData():
    print("Введите число n:")

    n = int(input())
    print("Введите матрицу - n строк по n чисел:")
    a = [list(map(float, input().split(' '))) for i in range(n)]

    return n, Matrix(a)


def main():
    n, a = readData()

    if not a.is_tridiag():
        print("Реализовано только для симметричных матриц :(")
        return

    qk, ak = threeDiagAlgo(a)
    print("Трёхдиагональная матрица A:")
    ak.printMatrix()
    print()

    print("Матрица Q^{(k)}:")
    qk.printMatrix()


if __name__ == "__main__":
    main()

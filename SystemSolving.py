from Matrix import Matrix
from Vector import Vector
from lib import GaussSeidel, simpleIter


def readData():
    print("Введите число n:")
    n = int(input())

    print("Введите матрицу - n строк по n чисел:")
    a = [list(map(float, input().split(' '))) for i in range(n)]

    print("Введите вектор b - n чисел в одну строку:")
    b = list(map(float, input().split(' ')))

    print("Введите точность:")
    e = float(input())

    return n, Matrix(a), Vector(b), e


def main():
    n, a, b, e = readData()
    resGS = GaussSeidel(n, a, b, e)
    if isinstance(resGS, str):
        resSI = simpleIter(n, a, b, e)
        if isinstance(resSI, str) :
            print("Sorry, we don't know how to solve this yet...")
        else:
            resSI.printVector()
    else:
        resGS.printVector()


if __name__ == "__main__":
    main()

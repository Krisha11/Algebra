from Matrix import Matrix
from Vector import Vector
from lib import QRGivens, QRHausholder


def readData():
    print("Введите число n:")
    n = int(input())

    print("Введите матрицу - n строк по n чисел:")
    a = [list(map(float, input().split(' '))) for i in range(n)]

    return n, Matrix(a)


def main():
    n, a = readData()
    q, r = None, None

    print("Какой алгоритм вы хотите использовать? Напишить одну из букв: G/H/A (с помощью вращений Гивенса/отражений Хаусхолдера/Любой.")
    ch = input()
    if ch == 'G' or ch == 'g' or ch == 'П' or ch == 'п':
        q, r = QRGivens(a)
    else:
        q, r = QRHausholder(a)

    print("Матрица Q:")
    q.printMatrix()
    print("Матрица R:")
    r.printMatrix()


if __name__ == "__main__":
    main()

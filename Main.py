import sys
import SystemSolving
import QRDecomposition
import MaxEigenvalueSearching
import QRAlgo
import Tridiagonalization


def main():
    if len(sys.argv) <= 1:
        print("Необходим флаг запуска")
        return
    flag = sys.argv[1]
    if flag == "simple_iteration":
        SystemSolving.main()
    elif flag == "qr_decomposition":
        QRDecomposition.main()
    elif flag == "qr_simple_iteration":
        MaxEigenvalueSearching.main()
    elif flag == "qr_algo":
        QRAlgo.main()
    elif flag == "tridiag":
        Tridiagonalization.main()
    else:
        print("Неправильный флаг запуска")


if __name__ == "__main__":
    main()

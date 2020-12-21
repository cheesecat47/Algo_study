import sys

matrix = None
path = None


def printMatrix():
    for i in matrix:
        print(i)

    for i in path:
        print(i)


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [[ch for ch in sys.stdin.readline().strip()] for _ in range(n)]
    path = [[0 for _ in range(m)] for _ in range(n)]
    printMatrix()

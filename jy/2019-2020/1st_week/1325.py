import sys


def printMatrix(m):
    for c in m:
        print(c)


def dfs(matrix, n):
    count = {}

    for i in range(n):
        stack = [i]
        visited = [-1 for _ in range(n)]
        max_len = 0

        while len(stack) > 0:
            this = stack.pop()
            visited[this] = 1
            max_len += 1

            for i in sorted(matrix[this], reverse=True):
                if visited[i] == -1:
                    visited[i] = 1
                    stack.append(i)


n, m = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a-1][b-1] = 1

printMatrix(matrix)

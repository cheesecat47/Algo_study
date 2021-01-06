def solution(m, n, puddles):
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for [x, y] in puddles:
        matrix[x][y] = -999
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                matrix[i][j] = 1
                continue
            if matrix[i][j] == -999:
                continue
            if matrix[i-1][j] == -999:
                matrix[i][j] = matrix[i][j-1]
            elif matrix[i][j-1] == -999:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    
    return matrix[m][n] % 1000000007


if __name__ == "__main__":
    import time

    start = time.time()
    print(solution(m=4, n=3, puddles=[[2,2]]), "/ time :", time.time() - start)
    # 4 / time : 1.8835067749023438e-05
def solution(triangle):
    
    n = len(triangle)
    m = [[-99999 for _ in range(n+1)] for _ in range(n+1)]
    l = [[-99999 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(n):
        j = 1
        for each in triangle[i]:
            m[i+1][j] = each
            j += 1
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                l[i][j] = m[i][j]
            else:
                l[i][j] = max(l[i-1][j-1], l[i-1][j]) + m[i][j]
    
    return max(l[n])


if __name__ == "__main__":
    import time

    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

    start = time.time()
    print(solution(triangle=triangle), "/ time :", time.time() - start)
    # 30 / time : 6.604194641113281e-05
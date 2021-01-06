def recursive_naive(i, j):
    if i == 1 and j == 1:
        return m[i][j]
    elif i == 1:
        return recursive_naive(1, j-1) + m[i][j]
    elif j == 1:
        return recursive_naive(i-1, 1) + m[i][j]
    else:
        return min(recursive_naive(i-1, j),
                   recursive_naive(i, j-1)) + m[i][j]


def recursive_cached(i, j):
    if l[i][j] != -1:
        return l[i][j]
    if i == 1 and j == 1:
        l[i][j] = m[i][j]
    elif i == 1:
        l[i][j] = recursive_cached(1, j-1) + m[i][j]
    elif j == 1:
        l[i][j] = recursive_cached(i-1, 1) + m[i][j]
    else:
        l[i][j] = min(recursive_cached(i-1, j),
                      recursive_cached(i, j-1)) + m[i][j]
    return l[i][j]


def bottom_up(i, j):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                l[i][j] = m[i][j]
            else:
                l[i][j] = min(l[i-1][j], l[i][j-1]) + m[i][j]
    return l[i][j]


def bottom_up_path(i, j):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                l[i][j] = m[i][j]
                p[i][j] = '-'
            else:
                if l[i-1][j] < l[i][j-1]:
                    l[i][j] = l[i-1][j] + m[i][j]
                    p[i][j] = '↑'
                else:
                    l[i][j] = l[i][j-1] + m[i][j]
                    p[i][j] = '←'
    return l[i][j]


def print_path_recursive(i, j):
    if p[i][j] == '-':
        print(i, j)
    else:
        if p[i][j] == '←':
            print_path_recursive(i, j-1)
        else:
            print_path_recursive(i-1, j)
        print(i, j)


if __name__ == "__main__":
    import time

    lim = 999

    n = 4
    m = [[lim, lim, lim, lim, lim],
         [lim, 6, 7, 12, 5],
         [lim, 5, 3, 11, 18],
         [lim, 7, 17, 3, 3],
         [lim, 8, 10, 14, 9]]

    start = time.time()
    print(recursive_naive(n, n), "time :", time.time() - start)
    # 40 time : 3.981590270996094e-05

    l = [[lim, lim, lim, lim, lim],
         [lim, -1, -1, -1, -1],
         [lim, -1, -1, -1, -1],
         [lim, -1, -1, -1, -1],
         [lim, -1, -1, -1, -1]]

    start = time.time()
    print(recursive_cached(n, n), "time :", time.time() - start)
    # 40 time : 3.790855407714844e-05

    l = [[lim, lim, lim, lim, lim],
         [lim, -1, -1, -1, -1],
         [lim, -1, -1, -1, -1],
         [lim, -1, -1, -1, -1],
         [lim, -1, -1, -1, -1]]

    start = time.time()
    print(bottom_up(n, n), "time :", time.time() - start)
    # 40 time : 2.5987625122070312e-05

    l = [[lim, lim, lim, lim, lim],
         [lim, -1, -1, -1, -1],
         [lim, -1, -1, -1, -1],
         [lim, -1, -1, -1, -1],
         [lim, -1, -1, -1, -1]]
    p = [[lim, lim, lim, lim, lim],
         [lim, -1, -1, -1, -1],
         [lim, -1, -1, -1, -1],
         [lim, -1, -1, -1, -1],
         [lim, -1, -1, -1, -1]]

    bottom_up_path(n, n)
    print_path_recursive(n, n)
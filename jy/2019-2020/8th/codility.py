def solution(N, A):
    delta = {}

    maxnum = 0
    curmax = 0
    prevmax = 0

    for i in A:
        if i == N + 1 and maxnum > 0:
            curmax = prevmax + maxnum
            prevmax = curmax
            delta.clear()
            maxnum = 0
            print('curmax{} prevmax {}'.format(curmax, prevmax))

        elif i <= N:
            delta[i] = delta.get(i, 0) + 1
            if maxnum < delta[i]:
                maxnum = delta[i]
        print('max {}'.format(maxnum))
        print(delta)

    B = [curmax for _ in range(N)]
    for k, v in delta.items():
        B[k-1] += v
    
    print(B)

    return B


if __name__ == "__main__":
    solution(5, [3, 4, 4, 6, 1, 4, 4])
    print()
    solution(5, [3, 4, 4, 6, 1, 4, 4, 6])
    print()
    solution(5, [6, 6, 6, 6, 6, 6])

def bfs(v):
    from collections import deque
    q = deque()
    q.appendleft(v)
    colour[v] = 1   # blue

    while q:
        this = q.pop()
        this_colour = colour[this]
        # print(this, hate[this])
        for i in hate[this]:
            # print(i, colour[i])
            if colour[i] == 0:
                colour[i] = -this_colour
                q.appendleft(i)


if __name__ == "__main__":
    import sys
    r = sys.stdin.readline

    n = int(r())
    hate = [[] for _ in range(n)]

    for i in range(n):
        temp = list(map(int, r().split()))
        for j in range(temp[0]):
            hate[i].append(temp[j+1]-1)

    blue = []
    white = []
    colour = [0 for _ in range(n)]

    for i in range(n):
        # print('\nbfs', i)
        if colour[i] == 0:
            bfs(i)

    print(colour.count(1))
    for i in range(n):
        if colour[i] == 1:
            print(i+1, end=' ')
    print()
    print(colour.count(-1))
    for i in range(n):
        if colour[i] == -1:
            print(i+1, end=' ')
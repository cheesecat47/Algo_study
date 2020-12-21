import sys


def g(li, m):
    if len(li) == 0:
        return 0
    o = len(li) % m

    if o == 0:
        return sum(li[m - 1::m]) * 2
    else:
        return sum(li[o - 1::m]) * 2


n, m = map(int, sys.stdin.readline().split())
b = sorted(list(map(int, sys.stdin.readline().split())))
po = [i for i in b if i > 0]
ne = sorted(-i for i in b if i < 0)
print(g(po, m) + g(ne, m) - max(abs(b[0]), abs(b[-1])))

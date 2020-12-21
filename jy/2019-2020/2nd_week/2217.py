import sys
n = int(sys.stdin.readline())
a = sorted([int(sys.stdin.readline()) for _ in range(n)])
i = m = 0
while i < n:
    w = a[i] * (n - i)
    if m < w:
        m = w
    i += 1
print(m)
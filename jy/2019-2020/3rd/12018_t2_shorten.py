import sys
r = sys.stdin.readline
n, m = map(int, r().split())
l = []
for i in range(n):
    t = {}
    t['p'], t['l'] = map(int, r().split())
    t['x'] = sorted(list(map(int, r().split())), reverse=True)[:t['l']][-1]
    l.append(t)
cnt = 0
d = []
for t in l:
    if t['p'] < t['l']:
        if m < 1: continue
        cnt += 1
        m -= 1
        d.append(l.index(t))
for k in d[::-1]:
    l.pop(k)
s = sorted(l, key=lambda x: x['x'])
for t in s:
    if m < t['x']: continue
    cnt += 1
    m -= t['x']
print(cnt)

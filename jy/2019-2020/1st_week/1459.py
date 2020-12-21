x, y, w, s = map(int, input().split())
mod = (x+y) % 2
ls, ss = max(x, y), min(x, y)
print(min((x + y) * w, (ls - mod) * s + mod * w, ss * s + (ls-ss) * w))

s = []
for _ in range(int(input())):
    i = int(input())
    s.append(i) if i else s.pop()       
print(sum(s))
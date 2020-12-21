def solution(number, k):
    stack = []
    for c in number:
        while k > 0 and stack and stack[-1] < c:
            stack.pop()
            k -= 1
        stack.append(c)

    for _ in range(k):
        stack.pop()
    return ''.join(stack)


if __name__ == "__main__":
    import sys
    r = sys.stdin.readline
    n, k = map(int, r().split())
    number = r().rstrip()
    print(solution(number, k))

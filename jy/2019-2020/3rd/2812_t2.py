def solution(number, k):
    answer = ''
    n = [int(i) for i in number]
    l = len(n) - k

    while len(n) > l :
        n.remove(min(n[:l]))

    for i in n:
        answer += str(i)

    return answer


if __name__ == "__main__":
    import sys
    n, k = map(int, sys.stdin.readline().split())
    number = sys.stdin.readline().rstrip()
    print(solution(number, k))

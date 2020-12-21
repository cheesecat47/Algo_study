def solution(number, k):
    answer = ''
    n = [int(i) for i in number]
    l = len(n) -1
    
    leftlen = k
    
    head, tail = 0, k - 1
    while leftlen > 0:
        print('h {} / t {} / l {}'.format(head, tail, leftlen))
        
        mIdx, mVal = 0, 0
        for i in range(head, tail):
            print(i, n[i])
            if mVal < n[i]:
                mIdx, mVal = i, n[i]
        print('mIdx {} / mVal {}'.format(mIdx, mVal))
        answer += str(mVal)
        
        leftlen -= mIdx - head
        print('leftlen {}'.format(leftlen))
        
        head = mIdx + 1
        tail = head + leftlen - 1
        print('h {} / t {} / l {}'.format(head, tail, leftlen))
    print('answer', answer)
    return answer

if __name__ == "__main__":
    import sys
    n, k = map(int, sys.stdin.readline().split())
    number = sys.stdin.readline().rstrip()
    solution(number, k)
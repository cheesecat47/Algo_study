if __name__ == "__main__":
    import sys
    n, m = map(int, sys.stdin.readline().split())

    lectures = []
    for i in range(n):
        temp = {}
        temp['p'], temp['l'] = map(int, sys.stdin.readline().split())
        temp['mi'] = list(map(int, sys.stdin.readline().split()))
        lectures.append(temp)
    print(lectures)

    cnt = 0
    for temp in lectures:
        if temp['p'] < temp['l']:
            if m < 1:
                # 마일리지 없으면 신청 불가
                continue
            # 수강 인원보다 적다면 1마일리지로 수강 가능
            cnt += 1
            m -= 1
    
    for temp in lectures:
        if temp['p'] == temp['l']:
            # 수강 인원과 신청 인원이 같다면
            # 그 중 가장 작은 마일리지만큼 신청할 때 성준이에게 우선순위
            min_mi = min(temp['mi'])
            print('min_mi', min_mi)
            if m < min_mi:
                continue
            cnt += 1
            m -= min_mi
        
    for temp in lectures:
        if temp['p'] > temp['l']:
            # 수강 인원보다 신청 인원이 많을 땐
            # 수강 인원 중 가장 작은 마일리지만큼
            sort_with_range = sorted(temp['mi'], reverse=True)[:temp['l']]
            print('swr', sort_with_range)
            min_mi = sort_with_range[3]
            print('min_mi', min_mi)
            if m < min_mi:
                continue
            cnt += 1
            m -= min_mi
        print('cnt {} m {}\n'.format(cnt, m))
    print(cnt)

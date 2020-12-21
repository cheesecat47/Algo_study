if __name__ == "__main__":
    import sys
    n, m = map(int, sys.stdin.readline().split())

    lectures = []
    for i in range(n):
        temp = {}
        temp['p'], temp['l'] = map(int, sys.stdin.readline().split())
        temp['mi'] = list(map(int, sys.stdin.readline().split()))
        temp['sorted_mi'] = sorted(temp['mi'], reverse=True)[:temp['l']]
        temp['min_mi'] = temp['sorted_mi'][-1]
        lectures.append(temp)
    # print(lectures)

    cnt = 0
    del_list = []
    for i in range(len(lectures)):
        temp = lectures[i]
        if temp['p'] < temp['l']:
            if m < 1:
                # 마일리지 없으면 신청 불가
                continue
            # 수강 인원보다 적다면 1마일리지로 수강 가능
            cnt += 1
            m -= 1
            del_list.append(i)

    for k in del_list[::-1]:
        # 선택한 후에 빼서 다음 정렬 쉽게.
        # 뒤에서부터 없애는 이유? 앞에서부터 빼면 인덱스 당겨져서 잘못 지움.
        lectures.pop(k)

    # print('lectures', lectures)
    sorted_lecture = sorted(lectures, key=lambda x: x['min_mi'])
    # print('sorted_lecture', sorted_lecture)
    
    for temp in sorted_lecture:
        # 수강 인원보다 신청 인원이 같거나 많을 땐
        # 수강 인원 중 가장 작은 마일리지만큼
        if m < temp['min_mi']:
            continue
        cnt += 1
        m -= temp['min_mi']
        # print('cnt {} m {}\n'.format(cnt, m))

    print(cnt)

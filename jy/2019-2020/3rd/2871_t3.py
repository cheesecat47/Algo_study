if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    cnt = [0 for _ in range(26)]
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    input_str = sys.stdin.readline().rstrip()
    sorted_arr = []
    for c in input_str[::-1]:
        sorted_arr.append(c)
        cnt[alpha.index(c)] += 1

    sk, hw = '', ''
    cnt_idx = 0
    for turn in range(n//2):
        sk_char = sorted_arr.pop(0)
        sk += sk_char
        cnt[alpha.index(sk_char)] -= 1

        while cnt[cnt_idx] == 0:
            cnt_idx += 1
        hw_char = alpha[cnt_idx]
        hw += hw_char
        cnt[alpha.index(hw_char)] -= 1
        sorted_arr.remove(hw_char)
        # print('sk', sk)
        # print('hw', hw)
        # print('sorted_arr', sorted_arr)
        # print('cnt', cnt)

    if hw < sk:
        print('DA')
    else:
        print('NE')
    print(hw)

if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    
    # 문자를 리스트로 만들고 뒤집음.
    arr1 = [c for c in sys.stdin.readline().rstrip()]
    arr1.reverse()

    # 알파벳 순으로 정렬
    arr2 = sorted(arr1)
    # print(arr1, arr2)

    sk, hw = '', ''
    for turn in range(n//2):
        sk_char = arr1.pop(0)
        sk += sk_char
        arr2.remove(sk_char)

        hw_char = arr2.pop(0)
        hw += hw_char
        arr1.remove(hw_char)

    if hw < sk:
        print('DA')
    else:
        print('NE')
    print(hw)

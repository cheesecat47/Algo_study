if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    ch = [c for c in sys.stdin.readline().rstrip()]

    sk, hw = '', ''
    for turn in range(n//2):
        sk += ch.pop()
        c = min(ch)
        hw += c
        ch.remove(c)

    if hw < sk:
        print('DA')
    else:
        print('NE')
    print(hw)

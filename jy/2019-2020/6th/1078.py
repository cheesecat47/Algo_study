if __name__ == "__main__":
    import sys
    di = int(sys.stdin.readline().rstrip())
    xi = di + 1
    while xi < 9999999:
        xr = int(str(xi)[::-1])
        if (xi - xr) == di:
            print(xi)
            quit(0)
        xi += 1
    print(-1)
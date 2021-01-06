# https://www.acmicpc.net/problem/7562

step = [[1, 2], [2, 1], [2, -1], [1, -2], 
        [-1, -2], [-2, -1], [-2, 1], [-2, 2]]

def process(this):
    src, dest = this[1], this[2]
    visited = [[0 for _ in range(this[0])] for _ in range(this[0])]
    cnt = [[0 for _ in range(this[0])] for _ in range(this[0])]

    q = []
    q.append(src)

    while q:
        cur_step = q.pop()
        cur_step_len = cnt[cur_step[0]][cur_step[1]]
        visited[cur_step[0]][cur_step[1]] = 1
        print('cur_step', cur_step, ' cur_step_len', cur_step_len)
        print('dest', dest)

        if cur_step == dest:
            return cur_step_len

        print()

if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    t = []

    for i in range(n):
        l = int(sys.stdin.readline())
        src_x, src_y = map(int, sys.stdin.readline().split())
        dest_x, dest_y = map(int, sys.stdin.readline().split())
        t.append([l, [src_x, src_y], [dest_x, dest_y]])

    for each in t:
        print(process(each))
        print()

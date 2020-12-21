import sys
r = sys.stdin.readline


def bfs(cur_pos: tuple):
    from collections import deque
    q = deque()
    q.appendleft(cur_pos)

    while q:
        this = q.pop()
        this_x, this_y = this
        if this == dst:
            break
        visited[this_x][this_y] = 1

        next_count = count[this_x][this_y] + 1
        next_list = [(this_x-2, this_y+1), (this_x-1, this_y+2), (this_x+1, this_y+2), (this_x+2, this_y+1),
                     (this_x-2, this_y-1), (this_x-1, this_y-2), (this_x+1, this_y-2), (this_x+2, this_y-1)]
        for each in next_list:
            each_x, each_y = each
            if each_x not in range(l) or each_y not in range(l):
                continue

            if next_count < count[each_x][each_y]:
                count[each_x][each_y] = next_count

            if visited[each_x][each_y] == 0:
                visited[each_x][each_y] = 1
                q.appendleft(each)


if __name__ == "__main__":
    test = int(r())
    for i in range(test):
        l = int(r())
        src = tuple(map(int, r().split()))
        dst = tuple(map(int, r().split()))

        if src == dst:
            print(0)
            continue

        visited = [[0 for _ in range(l)] for _ in range(l)]
        count = [[999 for _ in range(l)] for _ in range(l)]

        count[src[0]][src[1]] = 0
        bfs(src)

        print(count[dst[0]][dst[1]])

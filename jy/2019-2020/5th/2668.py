def dfs(v: int, visited: list, rec: list, root: int, flag:bool) -> bool:
    visited[v] += 1
    rec.append(v)
    for u in range(n):
        if matrix[v][u] == 1:
            if u == root:
                return True
            if visited[u] == 0:
                return dfs(u, visited, rec, root, flag)


if __name__ == "__main__":
    import sys
    r = sys.stdin.readline

    n = int(r())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        j = int(r()) - 1
        matrix[i][j] = 1

    answer = []
    for i in range(n):
        visited = [0 for _ in range(n)]
        rec = []
        flag = dfs(i, visited, rec, i, False)

        if flag:
            answer += rec
    
    ans_list = sorted(list(set(answer)))

    print(len(ans_list))
    for i in ans_list:
        print(i + 1)
    
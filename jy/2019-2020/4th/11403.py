def print_matrix(m: list) -> None:
    for r in m:
        for c in r:
            print(c, end=' ')
        print()


def dfs(v: int, visited: list, connected: list) -> None:
    visited[v] = 1
    for u in range(n):
        if input_graph[v][u] == 1:
            connected[u] = 1
            if visited[u] == 0:
                dfs(u, visited, connected)


if __name__ == "__main__":
    import sys
    r = sys.stdin.readline
    n = int(r())

    input_graph = [list(map(int, r().split())) for _ in range(n)]
    output_graph = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        visited = [0 for _ in range(n)]
        connected = [0 for _ in range(n)]

        dfs(i, visited, connected)
        
        for j in range(n):
            if connected[j] == 1:
                output_graph[i][j] = 1
    
    print_matrix(output_graph)

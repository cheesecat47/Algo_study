graph = {}
visited = None

not_visited_vertex = -1
visited_vertex = 1

def dfs(u):
    stack = [u]

    while stack:
        this = stack.pop()
        if visited[this] == not_visited_vertex:
            visited[this] = visited_vertex
            print(this, end=' ')

            for i in sorted(graph[this], reverse=True):
                if visited[i] == not_visited_vertex:
                    stack.append(i)

def bfs(u):
    from collections import deque
    q = deque()
    q.appendleft(u)

    while q:
        this = q.pop()
        visited[this] = visited_vertex
        print(this, end=' ')

        for i in sorted(graph[this]):
            if visited[i] == not_visited_vertex:
                visited[i] = visited_vertex
                q.appendleft(i)


if __name__ == "__main__":
    import sys
    n, m, v = map(int, sys.stdin.readline().rstrip().split())

    for i in range(m):
        v1, v2 = map(int, sys.stdin.readline().split())
        if v1 not in graph:
            graph[v1] = []
        graph[v1].append(v2)
        if v2 not in graph:
            graph[v2] = []
        graph[v2].append(v1)

    visited = [not_visited_vertex for _ in range(n+1)]
    dfs(v)

    print()
    visited = [not_visited_vertex for _ in range(n+1)]
    bfs(v)

graph = {}
visited = []
dfs_result = []
bfs_result = []


def dfs(u):
    stack = [u]

    while len(stack) > 0:
        this = stack.pop()
        dfs_result.append(this)
        visited[this] = 1

        for i in sorted(graph[this], reverse=True):
            if visited[i] == -1:
                visited[i] = 1
                stack.append(i)


def bfs(u):
    from collections import deque
    q = deque()
    q.appendleft(u)

    while len(q) > 0:
        this = q.pop()
        bfs_result.append(this)
        visited[this] = 1

        for i in sorted(graph[this]):
            if visited[i] == -1:
                visited[i] = 1
                q.appendleft(i)


if __name__ == "__main__":
    n, m, v = map(int, input().split())

    for i in range(m):
        v1, v2 = map(int, input().split())
        if v1 not in graph:
            graph[v1] = []
        graph[v1].append(v2)
        if v2 not in graph:
            graph[v2] = []
        graph[v2].append(v1)

    for _ in range(n+1):
        visited.append(-1)

    dfs(v)
    print(' '.join([str(i) for i in dfs_result]))

    visited.clear()
    for _ in range(n+1):
        visited.append(-1)

    bfs(v)
    print(' '.join([str(i) for i in bfs_result]))

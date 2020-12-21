import heapq


def prim(s):
    sum = 0
    q = []
    visited = [0 for _ in range(n)]

    visited[s-1] = 1
    for u in adj[s]:
        heapq.heappush(q, u)

    while q:
        wi, vi = heapq.heappop(q)
        if visited[vi-1] == 0:
            visited[vi-1] = 1
            sum += wi
            for u in adj[vi]:
                heapq.heappush(q, u)
        
    return sum


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    # build an adjacency list
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        v1, v2, w = map(int, input().split())
        adj[v1].append([w, v2])
        adj[v2].append([w, v1])

    # print('adj')
    # for i in adj:
    #     print(i)

    # Prim's algorithm
    print(prim(1))

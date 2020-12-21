import heapq
import sys
taken = None  # for prevent cycles
q = []


def process(v):
    taken[v] = 1
    for each in adj[v]:
        if taken[each[1]] == 0:
            heapq.heappush(q, each)


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    # build an adjacency list
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        v1, v2, w = map(int, sys.stdin.readline().split())
        adj[v1].append([w, v2])
        adj[v2].append([w, v1])

    # Prim's algorithm
    taken = [0 for _ in range(n+1)]
    process(1)
    mst_cost = 0
    while q:
        wi, vi = heapq.heappop(q)
        if taken[vi] == 0:
            mst_cost += wi
            process(vi)
    print(mst_cost)

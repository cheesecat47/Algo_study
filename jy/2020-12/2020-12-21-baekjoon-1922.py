# https://www.acmicpc.net/problem/1922

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add(self, src, dest, weight):
        if src not in self.graph:
            self.graph[src] = {}
        self.graph[src][dest] = weight

    def kruskal(self):
        # https://www.weeklyps.com/entry/%ED%81%AC%EB%A3%A8%EC%8A%A4%EC%B9%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Kruskals-algorithm
        
        print()

    def __str__(self) -> str:
        return str(self.graph)


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    g = Graph()

    for i in range(m):
        a, b, c = map(int, input().split())
        g.add(a, b, c)

    print(g)
    p = g.dfs(1)
    print('p:', p)
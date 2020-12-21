def dfs(v, n, computers, visited):
    visited[v] = 1
    for i in range(n):
        if computers[v][i] == 1 and visited[i] == 0:
            # 연결돼있는데 방문하지 않았다면
            dfs(i, n, computers, visited)
        

def solution(n, computers):
    answer = 0
    
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            dfs(i, n, computers, visited)
    
    return answer

if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))
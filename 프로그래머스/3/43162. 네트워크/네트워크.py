from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0]*(n)
    def BFS(v):
        q= deque()
        q.append(v)
        while q:
            a = q.popleft()
            visited[a]=1
            for j in range(n):
                if computers[a][j]==1 and visited[j]==0:
                    q.append(j)
                
    for i in range(n):
        if visited[i]==0:
            BFS(i)
            answer+=1
    
    return answer
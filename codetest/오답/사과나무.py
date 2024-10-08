from collections import deque
q = deque()
answer = 0
n = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
visited = [[0]*n for _ in range(n)]
dis = [[0]*n for _ in range(n)]
# print(graph)
q.append((n//2,n//2))
answer += graph[n//2][n//2]
visited[n//2][n//2] = 1
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if visited[nx][ny]==0 and dis[x][y]< n//2:
                dis[nx][ny] = dis[x][y]+1
                answer+=graph[nx][ny]
                q.append((nx,ny))
                visited[nx][ny] = 1
            
print(answer)

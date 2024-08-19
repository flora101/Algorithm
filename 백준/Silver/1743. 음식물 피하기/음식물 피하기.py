from collections import deque
q= deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m,k = map(int,input().split())
graph = [[0]*(m) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]
for i in range(k):
    a,b = map(int,input().split())
    graph[a-1][b-1]=1

result = []

def BFS(s_x,s_y):
    cnt = 0
    q.append((s_x,s_y))
    visited[s_x][s_y]= 1
    while q:
        x,y = q.popleft()
        cnt+=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0 and graph[nx][ny]==1:
                    visited[nx][ny] =1
                    q.append((nx,ny))
    result.append(cnt)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j]==0:
            BFS(i,j)
print(max(result))
from collections import deque
n = int(input())
graph = []
dx= [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    graph.append(list(map(int,input().split())))
max1, min1 = -2147000000,2147000000

for i in range(n):
    for j in range(n):
        max1= max(max1, graph[i][j])
        min1= min(min1, graph[i][j])
# print(max1,min1)
def BFS(s_x,s_y,bound):
    q.append((s_x,s_y))
    visited[s_x][s_y]=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]>bound and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    
result = []
for i in range(min1,max1+1):
    visited = [[0]*(n) for _ in range(n)]
    q= deque()
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k]>i and visited[j][k]==0:
                cnt+=1
                BFS(j,k,i)
    result.append(cnt)
print(max(result))

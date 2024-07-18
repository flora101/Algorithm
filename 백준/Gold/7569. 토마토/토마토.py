import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int,input().split())
graph = [[list(map(int,input().split())) for j in range(n)] for i in range(h)]
# print(graph)
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
queue = deque()

def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0<=nx<=n-1 and 0<=nz<=h-1 and 0<=ny<=m-1 and graph[nz][nx][ny]==0:
                graph[nz][nx][ny] = graph[z][x][y]+1
                queue.append((nz,nx,ny))


for i in range(h):
    for j in range(n):
        for k in range(m):
             if graph[i][j][k] == 1:
                queue.append((i,j,k))
bfs()

# print(graph)

cnt = 0
complete = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==0:
                complete=False
            cnt=max(cnt,graph[i][j][k])
if complete == False:
    print(-1)
else:
    print(cnt-1)
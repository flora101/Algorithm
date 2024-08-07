import sys
from collections import deque
input = sys.stdin.readline
m,n = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(n)]
check = [[0]*(m) for i in range(n)]
q=deque()
dx= [-1,1,0,0]
dy= [0,0,-1,1]
cnt=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            q.append((i,j))

while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=ny<m and 0<=nx<n:
            if graph[nx][ny]==0:
                q.append((nx,ny))
                graph[nx][ny]=1
                check[nx][ny]=check[x][y]+1
# print(graph)
flag =True
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            flag= False
            break
if flag==False:
    print("-1")
else:
    max1= -2147000000
    for i in range(n):
        for j in range(m):
            max1= max(max1,check[i][j])
    print(max1)

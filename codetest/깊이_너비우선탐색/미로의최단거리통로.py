import sys
from collections import deque
graph = [list(map(int,input().split())) for i in range(7)]
dis = [[0]*7 for _ in range(7)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
q=deque()
q.append((0,0))
dis[0][0]=0
while q:
    x,y = q.popleft()
    if x==6 and y==6:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<7 and 0<=ny<7:
            if graph[nx][ny]==0:
                graph[nx][ny]=1
                dis[nx][ny] = dis[x][y]+1
                q.append((nx,ny))
if dis[6][6]==0:
    print("-1")
else:
    print(dis[6][6])

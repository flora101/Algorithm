import sys
from collections import deque
graph = [list(map(int,input().split())) for i in range(7)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph[0][0]=1
cnt = 0
def DFS(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<7 and 0<=ny<7:
            if graph[nx][ny]==0:
                graph[nx][ny]=1
                DFS(nx,ny)
                graph[nx][ny]=0
DFS(0,0)
print(cnt)

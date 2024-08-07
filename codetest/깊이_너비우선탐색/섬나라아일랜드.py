import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
graph = [list(map(int,input().split())) for i in range(n)]
q= deque()
dx=[0,0,-1,1,1,-1,1,-1]
dy=[-1,1,0,0,1,-1,-1,1]
cnt=0
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            q.append((i,j))
            graph[i][j]=0
            while q:
                x,y=q.popleft()
                for k in range(8):
                    nx= x+dx[k]
                    ny = y+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny]==1:
                            q.append((nx,ny))
                            graph[nx][ny]=0
            cnt+=1
print(cnt)

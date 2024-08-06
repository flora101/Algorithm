import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,0,1,0]
dy = [0,1,0,-1]
ch = [[0]*n for _ in range(n)]
sum1= 0 
q = deque()
ch[n//2][n//2]=1
sum1 += graph[n//2][n//2]
q.append((n//2,n//2))
L=0
while True:
    if L==(n//2):
        break
    size = len(q)
    for j in range(size):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ch[nx][ny]==0:
                ch[nx][ny]=1
                # print(graph[nx][ny])
                sum1+=graph[nx][ny]
                q.append((nx,ny))
    L+=1

print(sum1)

import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
graph = [list(map(int,input().split())) for i in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
min1= 2147000000
max1= -2147000000
for i in range(n):
    min1 = min(min1,min(graph[i]))
    max1= max(max1, max(graph[i]))
    
ans=[]
for i in range(min1+1,max1-1):
    q=deque()
    ch = [[0]*(n) for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k]>i and ch[j][k]==0:#여기서 check확인 꼭 하기!
                q.append((j,k))
                ch[j][k]=1
                while q:
                    x,y = q.popleft()
                    for e in range(4):
                        nx=x+dx[e]
                        ny=y+dy[e]
                        if 0<=nx<n and 0<=ny<n:
                            if ch[nx][ny]==0 and graph[nx][ny]>i:
                                ch[nx][ny]=1
                                q.append((nx,ny))
                #                 cnt+=1
                # print(cnt)
                cnt+=1
    ans.append(cnt)
print(max(ans))

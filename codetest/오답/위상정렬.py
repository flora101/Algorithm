from collections import deque
q= deque()
n,m = map(int,input().split())
graph = [[0]*(n) for i in range(n)]
visited = [0]*(n)
for i in range(m):
    a,b = map(int,input().split())
    graph[a-1][b-1]=1
    visited[b-1]+=1
for i in range(n):
    if visited[i]==0:
        q.append(i)
while q:
    e = q.popleft()
    print(e+1,end=" ")
    for j in range(n):
        if graph[e][j]==1:
            visited[j]-=1
            if visited[j]==0:
                q.append(j)

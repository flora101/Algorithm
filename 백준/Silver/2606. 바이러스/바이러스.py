from collections import deque
q= deque()
com = int(input())
net = int(input())
graph = [[] for _ in range(com+1)]
for i in range(net):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(com+1)
cnt = 0
def BFS(v):
    global cnt
    q.append(v)
    visited[v]=1
    while q:
        cnt+=1
        x = q.popleft()
        for i in graph[x]:
            if visited[i]==0:
                visited[i]=1
                q.append(i)
BFS(1)
print(cnt-1)

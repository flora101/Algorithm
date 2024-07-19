import sys
input = sys.stdin.readline
from collections import deque

f,s,g,u,d = map(int,input().split())
cnt = 0
# visited = [0 for _ in range(f + 1)]  
visited = [0]*(f+1)


def bfs():
    q = deque()
    q.append(s)
    visited[s]=1
    go = False
    while q:
        x = q.popleft()
        if x == g:
            print(visited[x]-1)
            go = True
            break
        for i in (x+u,x-d):
            if 0<i<=f and visited[i]==0:
                visited[i]=visited[x]+1
                q.append(i)
    if go == False:
        print("use the stairs")
bfs()
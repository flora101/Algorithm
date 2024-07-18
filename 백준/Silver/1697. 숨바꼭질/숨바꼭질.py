import sys
input = sys.stdin.readline
from collections import deque

max_size = 100000
visited = [0] * (max_size+1)

n,k = map(int,input().split())
def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for i in [x-1, x+1, x*2]:
            if 0<=i<=max_size and visited[i]==0:
                q.append(i)
                visited[i]=visited[x]+1
bfs()
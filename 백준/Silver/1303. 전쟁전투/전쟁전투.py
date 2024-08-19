from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n, m = map(int,input().split())
graph = [list(input()) for _ in range(m)]
visited = [[0]*(n) for _ in range(m)]
# print(graph)
q = deque()
w_result = []
def BFS(s_x,s_y,team):
    cnt = 0
    q.append((s_x,s_y))
    visited[s_x][s_y]=1
    while q:
        cnt+=1
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if visited[nx][ny]==0 and graph[nx][ny]==team:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    w_result.append(cnt)

for i in range(m):
    for j in range(n):
        if graph[i][j]=="W" and visited[i][j]==0:
            BFS(i,j,"W")
# print(w_result)
wv = 0
for i in w_result:
    wv +=i**2
    
w_result = []
for i in range(m):
    for j in range(n):
        if graph[i][j]=="B" and visited[i][j]==0:
            BFS(i,j,"B")
# print(w_result)
bv= 0 
for i in w_result:
    bv +=i**2
    
print(wv,bv)

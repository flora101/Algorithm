import sys
graph = []
dx = [0,0,-1]
dy = [-1,1,0]
for i in range(10):
    graph.append(list(map(int,input().split())))
visited = [[0]*(10) for _ in range(10)]
for i in range(10):
    if graph[9][i]==2:
        start = (9,i)
# print(start)
def DFS(s_x,s_y):
    visited[s_x][s_y]=1
    if s_x == 0:
        print(s_y)
        sys.exit(0)
    for i in range(3):
        nx = s_x+dx[i]
        ny = s_y+dy[i]
        if 0<=nx<10 and 0<=ny<10:
            if graph[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny]=1
                DFS(nx,ny)
                visited[nx][ny]=0
DFS(start[0],start[1])

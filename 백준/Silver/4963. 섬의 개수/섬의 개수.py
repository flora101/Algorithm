import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [-1,1,0,0,1,-1,-1,1]
dy = [0,0,-1,1,1,-1,1,-1]

def dfs(x,y):
    visited[x][y]=1
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<=b-1 and 0<=ny<=a-1 and visited[nx][ny]==0 and graph[nx][ny]==1:
            visited[nx][ny]=1
            dfs(nx,ny)
            
while 1:
    a,b = map(int,input().split())
    if a ==0 and b==0:
        break
    graph=[]
    visited = [[0]*a for i in range(b)]
    cnt=0
    for i in range(b):
        graph.append(list(map(int,input().split())))
    for i in range(b):
        for j in range(a):
            if graph[i][j]==1 and visited[i][j]==0:
                cnt+=1
                visited[i][j]==1
                dfs(i,j)
    print(cnt)
    
import sys
input =sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph=[]
visited=[[0]*n for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
sum1=0
sum2=0

for i in range(n):
    graph.append(list(input().rstrip()))
# print(graph)

def dfs(x,y,color):
    visited[x][y]=1
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= n-1 and visited[nx][ny]==0:
            if graph[nx][ny]==color:
                dfs(nx,ny,color)

for color in ['R','G','B']:
    for i in range(n):
        for j in range(n):
            if graph[i][j]==color and visited[i][j]==0:
                dfs(i,j,color)
                sum1 +=1

for i in range(n):
    for j in range(n):
        if graph[i][j]=="G":
            graph[i][j]="R"
            
visited = [[0]*n for i in range(n)]

for color in ['R','B']:
    for i in range(n):
        for j in range(n):
            if graph[i][j]==color and visited[i][j]==0:
                dfs(i,j,color)
                sum2 +=1
print(sum1,sum2)
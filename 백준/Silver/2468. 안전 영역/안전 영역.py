import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
h=0
graph=[]
result =[]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    graph.append(list(map(int,input().split())))

# print(graph)
for i in graph:
    h = max(max(i),h)
# print(h)

def dfs(x,y,height):
    visited[x][y]=1
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if 0<=nx<=n-1 and 0<=ny<=n-1 and visited[nx][ny]==0 and graph[nx][ny]>height:
            visited[nx][ny]=1
            dfs(nx,ny,height)

for i in range(h):
    visited = [[0]*(n) for i in range(n)]
    cnt=0
    for j in range(n):
        for k in range(n):
            if graph[j][k]>i and visited[j][k]==0:
                cnt+=1
                visited[j][k]=1
                dfs(j,k,i)
    result.append(cnt)
print(max(result))
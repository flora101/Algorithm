import sys
input = sys.stdin.readline
n=int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
start=[0,0]
end=[0,0]
cnt=0
for i in range(n):
    for j in range(n):
        if graph[i][j]<graph[start[0]][start[1]]:
            start[0],start[1]=i,j
        if graph[i][j]>graph[end[0]][end[1]]:
            end[0],end[1]=i,j
dx= [0,1,0,-1]
dy = [-1,0,1,0]
check = [[0]*(n) for i in range(n)]

check[start[0]][start[1]]=1
# print(start,end)
def DFS(x,y):
    global cnt
    if x==end[0] and y == end[1]:
        cnt+=1
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]>graph[x][y] and check[nx][ny]==0:
                    check[nx][ny]=1
                    DFS(nx,ny)
                    check[nx][ny]=0
DFS(start[0],start[1])
print(cnt)

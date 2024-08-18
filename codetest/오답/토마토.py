from collections import deque
n,m = map(int,input().split())
apple=[]
dx= [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0]*(n) for i in range(m)]
day = [[0]*(n) for i in range(m)]
q =deque()
for i in range(m):
    apple.append(list(map(int,input().split())))
    
def BFS():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if visited[nx][ny]==0 and apple[nx][ny]==0 and day[nx][ny]==0:
                    # print(day)
                    visited[nx][ny]=1
                    apple[nx][ny]=1
                    day[nx][ny] = day[x][y]+1
                    q.append((nx,ny))
    
for i in range(m):
    for j in range(n):
        if apple[i][j]==1:
            q.append((i,j))

BFS()
flag = True
for i in range(m):
    for j in range(n):
        if apple[i][j] == 0:
            flag = False
            break

max1= -2147000000
if flag == False:
    print(-1)
else:
    for i in range(m):
        for j in range(n):
            max1= max(max1,day[i][j])
    print(max1)
# print(day)

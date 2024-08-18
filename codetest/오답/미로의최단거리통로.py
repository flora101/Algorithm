from collections import deque
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(7):
    graph.append(list(map(int,input().split())))
visited = [[0]*(7) for _ in range(7)]
dis = [[0]*(7) for _ in range(7)]
q = deque()
q.append((0,0))
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<7 and 0<=ny<7:
            if visited[nx][ny]==0 and graph[nx][ny]==0:
                q.append((nx,ny))
                dis[nx][ny] = dis[x][y]+1
                visited[nx][ny]=1
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])

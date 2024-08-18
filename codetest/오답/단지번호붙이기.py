# # BFS 풀이
# from collections import deque
# n = int(input())
# graph = []
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# q = deque()
# for _ in range(n):
#     graph.append(list(map(int,input())))
# # print(graph)
# visited = [[0]*(n) for _ in range(n)]
# result = []
# def BFS(s_x,s_y):
#     cnt = 0
#     visited[s_x][s_y]=1 # 자꾸 얘 까먹지 말것??!!!
#     q.append((s_x,s_y))
#     while q:
#         x, y = q.popleft()
#         cnt+=1
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0<=nx<n and 0<=ny<n:
#                 if visited[nx][ny]==0 and graph[nx][ny]==1:
#                     visited[nx][ny]=1
#                     q.append((nx,ny))
#     # print(cnt)
#     return cnt
# a = 0
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1 and visited[i][j]==0:
#             a+=1
#             result.append(BFS(i,j))
# print(a)
# print(result)


# DFS 풀이
n = int(input())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    graph.append(list(map(int,input())))
visited = [[0]*(n) for _ in range(n)]
result = []
def DFS(s_x,s_y):
    global cnt
    visited[s_x][s_y]=1
    for i in range(4):
        nx = s_x+dx[i]
        ny = s_y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if visited[nx][ny]==0 and graph[nx][ny]==1:
                visited[nx][ny]=1
                cnt+=1
                DFS(nx,ny)
                visited[nx][ny]=1
    return cnt
    
ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visited[i][j]==0:
            ans+=1
            cnt = 1
            result.append(DFS(i,j))

print(ans)
for i in result:
    print(i)

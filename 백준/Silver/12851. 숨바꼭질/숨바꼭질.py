import sys
from collections import deque
n,m = map(int,input().split())
dis = [0]*(100001)
# print(dis)
q=deque()
cnt = 0
def BFS(v):
    global cnt
    q.append(v)
    dis[v]=1
    while q:
        e = q.popleft()
        if e == m:
            cnt+=1
        for i in [e-1,e+1,e*2]:
            if 0<=i<=100000 and (dis[i]==0 or dis[i]==dis[e]+1):
                dis[i]=dis[e]+1
                q.append(i)
BFS(n)
print(dis[m]-1)
print(cnt)


# import sys
# from collections import deque
# n,m = map(int,input().split())
# dis = [0]*(100001)
# visited = [0]*(100001)
# # print(visited)
# # print(dis)
# q=deque()
# def BFS(v):
#     q.append(v)
#     visited[v]=1
#     while q:
#         e = q.popleft()
#         if e == m:
#             print(dis[e])
#             break
#         # sys.exit()
#         for i in [e-1,e+1,e*2]:
#             if 0<=i<=100000 and visited[i]==0:
#                 visited[i]=1
#                 dis[i]=dis[e]+1
#                 q.append(i)
# BFS(n)

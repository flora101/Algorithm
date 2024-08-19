# 메모리 초과 뜬 코드
# from collections import deque
# a,b = map(int,input().split())
# q = deque()
# visited = [0]*(b+1)
# ans=0
# def BFS(v):
#     global ans
#     q.append(v)
#     visited[v]=1
#     while q:
#         e = q.popleft()
#         if e > b:
#             continue
#         if e == b:
#             ans = visited[e]
#             break
#         for i in [e*2,int(str(e)+'1')]:
#             if 0<=i<=b and visited[i]==0:
#                 visited[i]=visited[e]+1
#                 q.append(i)
# BFS(a)
# if ans == 0:
#     print("-1")
# else:
#     print(ans)


from collections import deque
a,b = map(int,input().split())
q = deque()
q.append((a,1))
r = 0

while(q):
    n,t = q.popleft()
    if n > b:
        continue
    if n == b:
        print(t)
        break
    q.append((int(str(n)+"1"),t+1))
    q.append((n*2,t+1))
else:
    print(-1)

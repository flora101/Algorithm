from collections import deque
s,e =map(int,input().split())
q = deque()
q.append(s)
pos = [-1,1,5]
visited = [0] * (10001)
dis = [0] *(10001)
visited[s]=1
cnt = 0
dis[s]=0
while q:
    a = q.popleft()
    if a == e:
        print(dis[a])
        break
    for i in pos:
        if 0<a+i<10000 and visited[a+i]==0:
            q.append(a+i)
            visited[a+i]=1
            dis[a+i]=dis[a]+1
# print(dis[e])

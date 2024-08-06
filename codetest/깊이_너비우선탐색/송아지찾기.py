import sys
from collections import deque
input =sys.stdin.readline
s,e = map(int,input().split())
q=deque()
MAX=10000
ch=[0]*(MAX+1)
dis=[0]*(MAX+1)
ch[s]=1
dis[s]=0
q.append(s)
while q:
    a = q.popleft()
    if a == e:
        break
    for i in (a-1,a+1,a+5):
        if 0<i<=MAX:#음수 좌표 없음
            if ch[i]==0: #방문 안했을때만
                q.append(i)
                ch[i]=1
                dis[i]=dis[a]+1
print(dis[e])

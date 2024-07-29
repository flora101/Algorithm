import sys
from collections import deque
input = sys.stdin.readline
n,m=map(int,input().split())
pat = [(pos,val) for pos,val in enumerate(list(map(int,input().split())))]
cnt=0
q=deque(pat)
while 1:
    cur=q.popleft()
    if any(cur[1]<x[1] for x in q):
        q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            break
print(cnt)

import sys
from collections import deque
input = sys.stdin.readline
n,k=map(int,input().split())
q = deque()
for i in range(1,n+1):
    q.append(i)
i=1
while len(q)>1:
    if i==k:
        q.popleft()
        i=1
    else:
        q.append(q.popleft())
        i+=1
print(q.pop())

import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
se=[]
q=deque()
for i in range(n):
    q.append(input().rstrip())
for i in range(n-1):
    a=input().rstrip()
    while 1:
        if a==q[0]:
            q.popleft()
            break
        else:
            q.append(q.popleft())
print(q.pop())

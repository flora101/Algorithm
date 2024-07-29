import sys
from collections import deque
input = sys.stdin.readline
ch=input()
ju=[]

n=int(input())
for i in range(n):
    plan=input()
    q=deque(ch)
    a=""
    for j in plan:
        if j in q:
            if j!=q.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(q)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))

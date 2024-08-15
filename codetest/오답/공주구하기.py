from collections import deque
n,k = map(int,input().split())
q = deque()
answer =[]
for i in range(1,n+1):
    q.append(i)
a = 1
while q:
    if a==k:
        answer.append(q.popleft())
        a =1
    else:
        q.append(q.popleft())
        a+=1
print(answer[-1])

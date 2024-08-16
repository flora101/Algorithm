from collections import deque
n,m = map(int,input().split())
people = list(map(int,input().split()))
q = deque()
answer = 0 #몇번째로 들어가는지
for i in range(n):
    q.append((i,people[i]))
while q:
    if any(q[0][1]<q[x][1] for x in range(len(q))): # any를 쓰자!!
        q.append(q.popleft())
    else:
        answer += 1
        if q[0][0]==m:
            print(answer)
            break
        q.popleft()

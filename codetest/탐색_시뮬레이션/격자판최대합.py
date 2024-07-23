import sys
input=sys.stdin.readline
n=int(input())
graph=[]
ans=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n):
    s=0
    a=0
    for j in range(n):
        a+=graph[j][i]
        s+=graph[i][j]
    ans.append(s)
    ans.append(a)
x=0
y=0
for i in range(n):
    for j in range(n):
        if i==j:
            x+=graph[i][j]
ans.append(x)
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            y+=graph[i][j]
ans.append(y)
print(max(ans))

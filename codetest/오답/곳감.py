n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
m=int(input())
for _ in range(m):
    ans=[]
    a,b,c=map(int,input().split())
    if b==0:
        for i in range(c):
            graph[a-1].append(graph[a-1].pop(0))
    else:
        for i in range(c):
            graph[a-1].insert(0,graph[a-1].pop())
# print(graph)
total=0
for i in range(n//2+1):
    for j in range(i,n-i):
        total+=graph[i][j]
for i in range(n//2+1,n):
    for j in range(n-1-i,i+1):
        total+=graph[i][j]
print(total)
            

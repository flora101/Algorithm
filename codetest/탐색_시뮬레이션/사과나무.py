import sys
input=sys.stdin.readline
n=int(input())
graph=[]
ans=0
for i in range(n):
    graph.append(list(map(int,input().split())))
n2 = n//2
for i in range(n//2+1):
    k=n2-i
    for j in range(i*2+1):
        ans+=graph[i][k]
        k+=1
# print(ans)
for i in range(n//2+1,n):
    k=i-n2
    for j in range((n-1-i)*2+1):
        # print(graph[i][k])
        ans+=graph[i][k]
        k+=1
print(ans)

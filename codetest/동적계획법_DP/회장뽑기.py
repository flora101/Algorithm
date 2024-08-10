import sys
input =sys.stdin.readline
n = int(input())
graph = [[50000]*(n+1) for i in range(n+1)]
ans=[]
while 1:
    a,b = map(int,input().split())
    if a==-1 and b==-1:
        break
    else:
        graph[a][b]= 1
        graph[b][a]=1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
# print(graph)
for i in range(1,n+1):
    max1 = 0
    for j in range(1,n+1):
        max1= max(max1,graph[i][j])
    ans.append(max1)
president = min(ans)
answer = []
for i in range(len(ans)):
    if ans[i] == president:
        answer.append(i+1)
print(president, len(answer))
print(" ".join(map(str,answer)))

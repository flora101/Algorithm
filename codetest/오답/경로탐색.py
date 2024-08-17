# n,m = map(int,input().split())
# graph = [[0]*(n) for _ in range(n)]
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     graph[a-1][b-1]=c
# for i in range(n):
#     for j in range(n):
#         print(graph[i][j],end = " ")
#     print()


n,m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
check =[0]*(n+1)
for _ in range(m):
    a,b= map(int,input().split())
    graph[a][b]=1
check[1] = 1
cnt = 0
def DFS(v):
    global cnt
    if v == n:
        cnt+=1
    else:
        for i in range(1,n+1):
            if graph[v][i]==1 and check[i]==0:
                check[i]=1
                DFS(i)
                check[i]=0
DFS(1)
print(cnt)

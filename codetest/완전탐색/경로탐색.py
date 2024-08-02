import sys
input =sys.stdin.readline
n,m = map(int,input().split())
graph = [[0]*(n+1) for i in range(n+1)]
ch = [0]*(n+1)
for i in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
cnt = 0
ch[1]=1

def DFS(v): #v = 노드 번호
    global cnt
    if v == n:
        cnt+=1
    else:
        for i in range(1,n+1):#방문노드 i
            if graph[v][i]==1 and ch[i]==0:
                ch[i]=1
                DFS(i)
                ch[i]=0
    
DFS(1)
print(cnt)

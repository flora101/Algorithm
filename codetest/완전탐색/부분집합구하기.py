import sys
input = sys.stdin.readline
n=int(input())
ch=[0]*(n+1)
def DFS(v):
    if v==n+1: #출력
        for i in range(1,n+1):
            if ch[i]==1:
                print(i,end=" ")
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)
DFS(1)

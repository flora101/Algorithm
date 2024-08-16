n,m = map(int,input().split())
check = [0]*(m)
cnt = 0
def DFS(L):
    global cnt
    if L == m:
        for i in check:
            print(i,end=" ")
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            check[L]=i
            DFS(L+1)
DFS(0)
print(cnt)

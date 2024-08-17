n,m  = map(int,input().split())
check = [0]*(n+1)
res = [0]*(m)
cnt= 0
def DFS(L,h):
    global cnt
    if L == m:
        for i in res:
            print(i,end=" ")
        print()
        cnt+=1
    else:
        for i in range(h+1,n+1):
            if check[i]==0:
                check[i]=1
                res[L]=i
                DFS(L+1,i)
                check[i]=0
    
DFS(0,0)
print(cnt)

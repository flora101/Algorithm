n,m = map(int,input().split())
check = [0]*(n+1)
answer= [0]*(m)
cnt = 0
def DFS(L):
    global cnt
    if L == m:
        # print(answer)
        # cnt+=1
        for i in range(L):
            print(answer[i],end=" ")
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if check[i]==0:
                check[i]=1
                answer[L]=i
                DFS(L+1)
                check[i]=0
DFS(0)
print(cnt)

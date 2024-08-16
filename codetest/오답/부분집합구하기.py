n = int(input())
check = [0]*(n)
def DFS(L):
    if L == n:
        # print(check)
        for i in range(n):
            if check[i] == 1:
                print(i+1,end=" ")
        print()
    else:
        check[L]=1
        DFS(L+1)
        check[L]=0
        DFS(L+1)
DFS(0)

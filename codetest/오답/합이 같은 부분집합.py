n = int(input())
num = list(map(int,input().split()))
total = sum(num)
flag = False
def DFS(L,sum1):
    global flag
    if sum1>total:
        return
    if L==n:
        if sum1*2 == total:
            flag = True 
            return
    else:
        DFS(L+1,sum1+num[L])
        DFS(L+1,sum1)
DFS(0,0)
if flag == True:
    print("YES")
else:
    print("NO")

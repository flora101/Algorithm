c,n = map(int,input().split())
weight = []
for i in range(n):
    weight.append(int(input()))
max1 = -2147000000
total=sum(weight)
def DFS(L,sum1,tsum): #tsum은 그냥 다 거쳐간 애들(넣든 안넣든)
    global max1
    if (total-tsum)+sum1 < max1:
        return 
    if sum1 >c:
        return 
    if L==n:
        if sum1<=c:
            max1= max(max1,sum1)
        return
    else:
        DFS(L+1,sum1+weight[L],tsum+weight[L])
        DFS(L+1,sum1,tsum+weight[L])
DFS(0,0,0)
print(max1)

import sys
input = sys.stdin.readline
n=int(input())
day=[]
money=[]
for i in range(n):
    a,b=map(int,input().split())
    day.append(a)
    money.append(b)
res=-2147000000
day.insert(0,0)
money.insert(0,0)
def DFS(L,sum1):
    global res
    if L==n+1:
        if sum1>res:
            res=sum1
    else:
        if L+day[L]<=n+1:
            DFS(L+day[L],sum1+money[L])
        DFS(L+1,sum1)
    
DFS(1,0)
print(res)

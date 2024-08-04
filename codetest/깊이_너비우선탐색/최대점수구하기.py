import sys
input = sys.stdin.readline
n,m = map(int,input().split())
pv=[]
pt=[]
for _ in range(n):
    score,time = map(int,input().split())
    pv.append(score)
    pt.append(time)
res = -2147000000
def DFS(L,sum,time):
    global res
    if time>m:
        return
    if L==n:
        if sum>res:
            res=sum
    else:
        DFS(L+1,sum+pv[L],time+pt[L])
        DFS(L+1,sum,time)
DFS(0,0,0)
print(res)

import sys
input = sys.stdin.readline
n=int(input())
money = []
ans=[0]*3
res=2147000000
for _ in range(n):
    a= int(input())
    money.append(a)
def DFS(L):
    global res
    if L == n:
        cha = max(ans)-min(ans)
        if cha<res:
            tmp=set()
            for x in ans:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
    else:
        for i in range(3):
            ans[i]+=money[L]
            DFS(L+1)
            ans[i]-=money[L]
DFS(0)
print(res)

import sys
input = sys.stdin.readline
t = int(input())
k = int(input())
cv,cn =[],[]
cnt = 0
for i in range(k):
    a,b= map(int,input().split())
    cv.append(a)
    cn.append(b)
def DFS(L,sum1):
    global cnt
    if sum1>t:
        return 
    if L==k:
        if sum1==t:
            cnt+=1
    else:
        for i in range(cn[L]+1):
            DFS(L+1,sum1+cv[L]*i)
DFS(0,0)
print(cnt)

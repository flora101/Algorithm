import sys
input=sys.stdin.readline
n,m = map(int,input().split())
res=[0]*(n)
ch=[0]*(n+1)
cnt=0
def DFS(L):
    global cnt
    if L==m:
        for i in range(L):
            print(res[i],end=" ")
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0 #다시되돌아온거->0으로 바꿔줘야함(앞이랑 대칭)
DFS(0)
print(cnt)

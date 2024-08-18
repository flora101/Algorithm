t=int(input())
k = int(input())
money,count =[],[]
for i in range(k):
    a,b =map(int,input().split())
    money.append(a)
    count.append(b)
cnt = 0
def DFS(L,m):
    global cnt
    if m>t:
        return
    if L == k:
        if m==t:
            cnt+=1
    else:
        for i in range(count[L]+1):
            DFS(L+1,m+money[L]*i)
DFS(0,0)
print(cnt)

n = int(input())
coin = []
money = [0,0,0]
for i in range(n):
    coin.append(int(input()))
min1 = 2147000000
def DFS(L,m):
    global min1
    if L == n:
        # print(m)
        if list(set(m))==m:
            if max(m)-min(m)<min1:
                min1 = max(m)-min(m)
    else:
        for i in range(3):
            m[i]+=coin[L]
            DFS(L+1,m)
            m[i]-=coin[L]
DFS(0,money)
print(min1)

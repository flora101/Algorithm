import sys
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
hs=[]
pz=[]
cb = [0]*m #조합
res= 2147000000
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            hs.append((i,j))
        elif board[i][j]==2:
            pz.append((i,j))
            
def DFS(L,s):
    global res
    if L==m:
        sum1 =0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis,abs(x1-x2)+abs(y1-y2))
            sum1 += dis
        if sum1<res:
            res= sum1
    else:
        for i in range(s,len(pz)):
            cb[L]=i
            DFS(L+1,i+1)

DFS(0,0)
print(res)

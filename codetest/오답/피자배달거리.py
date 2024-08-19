n,m=map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
pz,h = [],[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            pz.append((i,j))
        elif graph[i][j]==1:
            h.append((i,j))
s_pz=[0]*(m)
res = 2147000000
def DFS(L,now):
    global res
    if L == m:
        # print(s_pz)
        sum1= 0
        for i in range(len(h)):
            x1 = h[i][0]
            y1 = h[i][1]
            dis = 2147000000
            for j in s_pz:
                x2=pz[j][0]
                y2 = pz[j][1]
                dis = min(dis,abs(x1-x2)+abs(y1-y2))
            sum1+=dis
        if sum1<res:
            res=sum1
    else:
        for i in range(now,len(pz)):
            s_pz[L]=i
            DFS(L+1,i+1)
DFS(0,0)
print(res)

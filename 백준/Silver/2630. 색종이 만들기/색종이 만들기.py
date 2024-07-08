import sys
input = sys.stdin.readline

n = int(input())
graph = []
x,y = 0,0
for i in range(n):
    graph.append(list(map(int,input().split())))
# print(graph)

def quad(g,N,a,b):
    global x,y
    for i in range(a,a+N):
        for j in range(b,b+N):
            if g[i][j]!= g[a][b]:
                N //= 2
                quad(g,N,a,b)
                quad(g,N,a,b+N)
                quad(g,N,a+N,b)
                quad(g,N,a+N,b+N)
                return #이거 한번 다 돌았으면 함수 종료 하려고
    if g[a][b]==0:
        x+=1
    else:
        y+=1
    # print(x,y)

quad(graph,n,0,0)
print(x)
print(y)
import sys
input = sys.stdin.readline

g1,g2=[],[]
n,m = map(int,input().split())
for i in range(n):
    g1.append(list(map(int,input().split())))
    
m,k = map(int,input().split())
for j in range(m):
    g2.append(list(map(int,input().split())))
    
# print(g1)
# print(g2)
result = [[0 for _ in range(k)] for _ in range(n)]
# print(result)

for i in range(n):
    for j in range(k):
        for e in range(m):
            result[i][j] += g1[i][e]*g2[e][j]

for i in result:
    for j in range(len(i)):
        print(i[j],end=" ")
    print()
# import sys
# input=sys.stdin.readline
# n=int(input())
# graph=[]
# ans=0
# for i in range(n):
#     graph.append(list(map(int,input().split())))
# m=int(input())
# for i in range(m):
#     a,b,c=map(int,input().split())
#     graph2=[0 for i in range(n)]
#     if b==0:
#         for j in range(n):
#             if j>=c:
#                 graph2[j-c]=graph[a-1][j]
#             else:
#                 graph2[j-c]=graph[a-1][j]
#         graph[a-1]=graph2
#     elif b==1:
#         for j in range(n):
#             if j+c<=n-1:
#                 graph2[j+c]=graph[a-1][j]
#             else:
#                 graph2[j+c-n]=graph[a-1][j]
#         graph[a-1]=graph2
# # print(graph)
# answer=0
# for i in range(n//2+1):
#     for j in range(i,n-i):
#         # print(graph[i][j])
#         answer+=graph[i][j]
# for i in range(n//2+1,n):
#     for j in range(n-1-i,i+1):
#         # print(graph[i][j])
#         answer+=graph[i][j]
# print(answer)

import sys
input=sys.stdin.readline
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h,t,k=map(int,input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0,a[h-1].pop())
# for x in a:
#     print(x)
res=0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)

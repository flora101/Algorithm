# import sys
# n,f = map(int,input().split())
# pa = [1] *(n)
# res = [0]*(n)
# check = [0]*(n+1)
# for i in range(1,n):
#     pa[i]=pa[i-1]*(n-i)//i
# ans = 0
# def DFS(L):
#     global ans
#     ans = 0
#     if L == n:
#         for i in range(n):
#             ans += res[i]*pa[i]
#         if ans == f:
#             print(res)
#             sys.exit()
#     else:
#         for i in range(1,n+1):
#             if check[i]==0:
#                 check[i]=1
#                 res[L]=i
#                 DFS(L+1)
#                 check[i]=0
# DFS(0)


import sys
from itertools import permutations
n,f = map(int,input().split())
pa = [1] *(n)
res = [0]*(n)
check = [0]*(n+1)
for i in range(1,n):
    pa[i]=pa[i-1]*(n-i)//i
ans = 0
per = (list(permutations(range(1,n+1))))
for j in per:
    ans = 0
    for i in range(n):
        ans+=pa[i]*j[i]
    if ans == f:
        for k in range(n):
            print(j[k],end=" ")
        break

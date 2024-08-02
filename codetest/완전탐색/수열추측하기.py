# import sys
# input = sys.stdin.readline
# n,f=map(int,input().split())
# # from itertools import combinations,permutations
# p=[0]*n
# b=[1]*n
# ch=[0]*(n+1)
# for i in range(1,n):
#     b[i]=b[i-1]*(n-i)//i
# # for x in b:
# #     print(x)
# def DFS(L,sum):
#     if L==n and sum==f:
#         for x in p:
#             print(x,end=" ")
#         print()
#     else:
#         for i in range(1,n+1):
#             if ch[i]==0:
#                 ch[i]=1
#                 p[L]=i
#                 DFS(L+1,sum+(p[L]*b[L]))
#                 ch[i]=0
# DFS(0,0)


# 순열 이용해서 문제 풀기
import sys
import itertools as it
input =sys.stdin.readline
n,f = map(int,input().split())
b=[1]*n
cnt=0
for i in range(1,n):
    b[i]=b[i-1]*(n-i)/i
a=list(range(1,n+1))
for tmp in it.permutations(a):
    sum=0
    for L,x in enumerate(tmp):
        sum+=(x*b[L])
    if sum ==f:
        for x in tmp:
            print(x,end=" ")
        break

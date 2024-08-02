# import sys
# input = sys.stdin.readline
# n,k = map(int,input().split())
# num = list(map(int,input().split()))
# m = int(input())
# res=[0]*(k)
# cnt=0
# def DFS(L,s):
#     global cnt
#     if L==k:
#         if sum(res)%m==0:
#             # print(res)
#             cnt+=1
#     else:
#         for i in range(s,n):
#             res[L]=num[i]
#             DFS(L+1,i+1)
# DFS(0,0)
# print(cnt)


import sys
import itertools as it
input = sys.stdin.readline
n,k = map(int,input().split())
a = list(map(int,input().split()))
m=int(input())
cnt = 0
for x in it.combinations(a,k):
    if sum(x)%6==0:
        cnt+=1
print(cnt)

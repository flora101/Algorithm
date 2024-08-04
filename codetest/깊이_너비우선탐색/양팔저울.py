# import sys
# input = sys.stdin.readline
# k=int(input())
# weight= list(map(int,input().split()))
# res=[]
# s=sum(weight)
# def DFS(L,sum1):
#     global res
#     if L == k:
#         if sum1 not in res and sum1>0:
#             res.append(sum1)
#     else:
#         DFS(L+1,sum1+weight[L])
#         DFS(L+1,sum1)
#         DFS(L+1,sum1-weight[L])
# DFS(0,0)
# # print(res)
# print(s-len(res))
#시간초과뜸..



import sys
input = sys.stdin.readline
k=int(input())
weight= list(map(int,input().split()))
res=set()
s=sum(weight)
def DFS(L,sum1):
    global res
    if L == k:
        if 0<sum1<=s:
            res.add(sum1)
    else:
        DFS(L+1,sum1+weight[L])
        DFS(L+1,sum1)
        DFS(L+1,sum1-weight[L])
DFS(0,0)
# print(res)
print(s-len(res))

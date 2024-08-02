# #시간초과뜸..
# import sys
# input = sys.stdin.readline
# n = int(input())
# money = list(map(int,input().split()))
# m = int(input())
# res = 2147000000
# money.sort(reverse=True)
# def DFS(L,sum):
#     global res
#     if sum>m:
#         return
#     elif sum == m:
#         res = min(res,L)
#     else:
#         for i in range(n):
#             DFS(L+1,sum+money[i])
#     return res
# print(DFS(0,0))




import sys
input = sys.stdin.readline
n = int(input())
money = list(map(int,input().split()))
m = int(input())
res = 2147000000
money.sort(reverse=True)
def DFS(L,sum):
    global res
    if L>res:
        return
    if sum>m:
        return
    elif sum == m:
        res = min(res,L)
    else:
        for i in range(n):
            DFS(L+1,sum+money[i])
    return res
print(DFS(0,0))

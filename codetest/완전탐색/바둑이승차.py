# import sys
# input = sys.stdin.readline
# c,n = map(int,input().split())
# weight=[]
# for i in range(n):
#     weight.append(int(input()))
# max_weight = 0
# def DFS(x,y):
#     global max_weight
#     if x==n and y<=c:
#         max_weight = max(max_weight,y)
#     else:
#         if y>c:
#             return
#         else:
#             DFS(x+1,y+weight[x])
#             DFS(x+1,y)
#             max_weight = max(max_weight,y)
#     return max_weight
# print(DFS(0,0))
##시간초과 뜸



 #조건추가해서 미리 가지치기 하기
import sys
from collections import deque
c,n = map(int,input().split())

def DFS(L,sum,tsum):
    global result
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n:
        if sum>result:#여기 result는 지역변수이므로 전역변수로 바꿔줘야됨
            result =sum
    else:
        DFS(L+1,sum+a[L],tsum+a[L])
        DFS(L+1,sum,tsum+a[L])
        
a=[0]*n
total=sum(a)
result = -2147000000
for i in range(n):
    a[i]=int(input())
DFS(0,0)
print(result)

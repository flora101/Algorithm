# # 몇개 시간초과 뜸..
# import sys
# from itertools import combinations
# input = sys.stdin.readline
# n,m=map(int,input().split())
# num=[]
# cnt = 0
# for i in range(1,n+1):
#     num.append(i)
# for x,y in list(combinations(num,m)):
#     print(x,y, end=" ")
#     cnt+=1
#     print()
# print(cnt)

import sys
input = sys.stdin.readline
n,m=map(int,input().split())
res=[0]*(n)
cnt= 0
def DFS(L,s):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j],end=" ")
        print()
        cnt+=1
    else:
        for i in range(s,n+1):
            res[L]=i
            DFS(L+1,i+1)
DFS(0,1)
print(cnt)

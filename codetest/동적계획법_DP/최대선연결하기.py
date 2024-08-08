# import sys
# input = sys.stdin.readline
# n= int(input())
# num = list(map(int,input().split()))
# cnt=0
# num.insert(0,0)
# m=0
# k=0
# for i in range(1,n+1):
#     for j in range(k+1,i+1):
#         if i==num[j] and m<num[j]:
#             cnt+=1
#             m=num[j]
#             k=j
#             print(i,j)
# print(cnt)


# 결국 최대 증가 수열이랑 동일한 문제 ㅠ
import sys
input = sys.stdin.readline
n= int(input())
num = list(map(int,input().split()))
num.insert(0,0)
dy = [0]*(n+1)
dy[1]=1
res=0
for i in range(2,n+1):
    max1=0
    for j in range(i-1,0,-1):
        if num[j]<num[i] and dy[j]>max1:
            max1=dy[j]
    dy[i]=max1+1
    if dy[i]>res:
        res=dy[i]
print(res)

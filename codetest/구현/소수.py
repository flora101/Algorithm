# import sys
# input = sys.stdin.readline
# n=int(input())
# cnt=0
# for i in range(2,n+1):
#     flag=True
#     for j in range(2,i):
#         if i%j==0:
#             flag=False
#             break
#     if flag == True:
#         cnt+=1
# print(cnt)
# #시간초과 뜸..

import sys
input = sys.stdin.readline
n=int(input())
num=[0]*(n+1)
cnt=0
for i in range(2,n+1):
    if num[i]==0:
        cnt+=1
        for j in range(i,n+1,i):
            num[j]=1
print(cnt)
#에라토스테네스의 체

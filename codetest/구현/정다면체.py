# import sys
# from collections import Counter
# input = sys.stdin.readline
# n,m = map(int,input().split())
# cnt = Counter()
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         cnt[i+j]+=1
# # print(cnt)
# mc = max(cnt.values())
# result = []
# for k,v in cnt.items():
#     # print(k,v)
#     if v == mc:
#         result.append(k)
# print(" ".join(map(str, result)))

import sys
from collections import Counter
input = sys.stdin.readline
n,m = map(int,input().split())
max=-2147000000
cnt = [0]*(n+m+3)
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1
for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=" ")

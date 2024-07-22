# import sys
# input = sys.stdin.readline
# n,m = map(int, input().split())
# num = list(map(int, input().split()))
# i,j=0,0
# cnt=num[i]
# answer=0
# while i<n and j<n:
#     if cnt < m:
#         j+=1
#         if j<n:
#             cnt+=num[j]
#     elif cnt > m:
#         cnt-=num[i]
#         i+=1
#     else:
#         answer+=1
#         cnt-=num[i]
#         i+=1
# print(answer)


import sys
input = sys.stdin.readline
n,m = map(int, input().split())
a = list(map(int, input().split()))
lt,rt=0,1
tot=a[0]
cnt=0
while 1:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1

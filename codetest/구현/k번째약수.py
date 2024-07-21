# import sys
# input = sys.stdin.readline

# n,k = map(int,input().split())
# answer=[]
# for i in range(n):
#     if n % (i+1)==0:
#         answer.append(i+1)
# # print(answer)
# if len(answer)<k:
#     print(-1)
# else:
#     print(answer[k-1])

import sys
#sys.stdin = open("learn\ch2\input.txt", "rt")
n,k = map(int,input().split())
cnt=0
for i in range(1,n+1):
    if n % i==0:
        cnt+=1
    if cnt ==k:
        print(i)
        break
else:
    print(-1)

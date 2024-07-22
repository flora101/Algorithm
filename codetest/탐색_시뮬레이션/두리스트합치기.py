import sys
input = sys.stdin.readline
n=int(input())
nl = list(map(int, input().split()))
m=int(input())
ml = list(map(int, input().split()))
answer=[]
i,j=0,0
# while 1:
#     if i>=n:
#         for k in range(j,m):
#             answer.append(ml[k])
#         break
#     if j>=m:
#         for k in range(i,n):
#             answer.append(nl[k])
#         break
#     if i<n and j<m:
#         if nl[i]<=ml[j]:
#             answer.append(nl[i])
#             i+=1
#         else:
#             answer.append(ml[j])
#             j+=1
# print(' '.join(map(str,answer)))

while i<n and j<m:
    if nl[i]<=ml[j]:
        answer.append(nl[i])
        i+=1
    else:
        answer.append(ml[j])
        j+=1
if i<n:
    answer+=nl[i:]
if j<m:
    answer+=ml[j:]
print(' '.join(map(str,answer)))

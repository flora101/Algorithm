# n,k = map(int,input().split())
# doll = list(map(int,input().split()))
# left,right = 0,0
# cnt = 0 #1의 개수
# answer = 2147000000 #가장 작은 집합 크기
# while right<n:
#     if doll[right]==1:
#         cnt+=1
#     while cnt >= k:
#         if cnt == k:
#             answer = min(answer, right - left + 1)
#         if doll[left] == 1:
#             cnt -= 1
#         left += 1
#     right += 1
# if answer ==2147000000:
#     print("-1")
# else:
#     print(answer)


n,k = map(int,input().split())
doll = list(map(int,input().split()))
left = 0
cnt = 0 #1의 개수
answer = 2147000000 #가장 작은 집합 크기
for right in range(n):
    if doll[right]==1:
        cnt+=1
    while cnt>k:
        if doll[left]==1:
            cnt-=1
        left+=1
    if cnt == k:
        while doll[left]==2:
            left+=1
        answer = min(answer,right-left+1)
if answer == 2147000000:
    print(-1)
else:
    print(answer)

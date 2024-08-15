k,n=map(int,input().split())
lan = []
for i in range(k):
    lan.append(int(input()))
min1,max1 = 1,max(lan)
answer=-2147000000
while min1<max1:
    mid1 = (min1+max1)//2
    cnt = 0
    for i in lan:
        cnt+=(i//mid1)
    if cnt<n:
        max1 = mid1-1
    else:
        if mid1>answer:
            answer = mid1
        min1 = mid1+1
        # print(min1,max1,answer)
print(answer)

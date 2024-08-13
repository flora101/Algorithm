n,m = map(int,input().split())
num = list(map(int,input().split()))
left,right = 0,1
cnt= 0 
total = num[0]
while right<=n:
    if total<m:
        if right<=n-1:
            total+=num[right]
            right+=1
        else:
            break
    elif total>m:
        total-=num[left]
        left+=1
    else:
        cnt+=1
        total-=num[left]
        left+=1
print(cnt)

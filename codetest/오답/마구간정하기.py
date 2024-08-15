n,c=map(int,input().split())
num =[]
for _ in range(n):
    num.append(int(input()))
num.sort()
left,right = num[0],num[-1]
answer=[]
def check(m):
    global cnt
    for i in range(1,n):
        if num[i]-num[ch[-1]]>=m:
            cnt+=1
            ch.append(i)
    if cnt>=c:
        return True
    return False

while left<=right:
    mid = (left+right)//2
    ch=[0]
    cnt = 1
    if check(mid)==False:
        right = mid-1
    else:
        # print(left,right,mid,answer)
        answer.append(mid)
        left = mid+1
print(max(answer))

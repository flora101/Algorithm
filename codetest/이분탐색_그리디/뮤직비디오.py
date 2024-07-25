import sys
input = sys.stdin.readline
n,m=map(int,input().split())
num = list(map(int,input().split()))
l,r=max(num),sum(num)
def hap(dvd,total): #dvd은 리스트
    cnt=1
    v=0
    for i in range(len(dvd)):
        if v+dvd[i]<=total:
            v+=dvd[i]
        else:
            v=0
            if v+dvd[i]<=total:
                v+=dvd[i]
            cnt+=1
    return cnt

# print(hap(num,15))
ans=[]
while l<=r:
    mid = (l+r)//2
    if hap(num,mid)<=m:
        ans.append(mid)
        r=mid-1
        # print(l,r,mid)
    else: #hap(num,mid)>m
        l=mid+1
print(min(ans))

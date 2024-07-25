import sys
input = sys.stdin.readline
n,c=map(int,input().split())
line=[]
def count(l):
    cnt=1
    ep=line[0]#제일 첫 말의 위치
    for i in range(1,n):
        if line[i]-ep>=l:
            cnt+=1
            ep=line[i]
    return cnt
for i in range(n):
    tmp=int(input())
    line.append(tmp)
line.sort()
lt=1
rt=line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)

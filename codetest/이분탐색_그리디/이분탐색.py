import sys
input = sys.stdin.readline
n,m=map(int,input().split())
num=list(map(int,input().split()))
l,r=0,n-1
num.sort()
while l<=r:
    s=(l+r)//2
    if m<num[s]:
        r=s-1
    elif m>num[s]:
        l=s+1
    else:
        print(s+1)
        break

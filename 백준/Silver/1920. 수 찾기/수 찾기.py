import sys
input = sys.stdin.readline

n=int(input())
num = list(map(int,input().split()))
m=int(input())
mum = list(map(int,input().split()))

num.sort()
for i in mum:
    left,right = 0,n-1
    find = False
    
    while left<=right:
        mid= (left+right)//2
        if i == num[mid]:
            find=True
            print(1)
            break
        elif i > num[mid]:
            left=mid+1
        else:
            right=mid-1
    if find ==False:
        print(0)
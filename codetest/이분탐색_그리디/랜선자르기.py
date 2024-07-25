import sys
input = sys.stdin.readline
k,n=map(int,input().split())
line=[]
for i in range(k):
    line.append(int(input()))
l,r=1,max(line)
res=[]
while l<=r:
    cnt=0
    b = (l+r)//2
    for i in range(k):
        cnt += line[i]//b
    if cnt<n:
        r=b-1
    else: #cnt>=n
        res.append(b)
        l=b+1
print(max(res))
            

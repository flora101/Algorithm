import sys
input = sys.stdin.readline
ch = input().rstrip()
ans = ""
for i in ch:
    if i.isdigit():
        ans+=i
ans = int(ans)
print(ans)
cnt=0
for i in range(1,ans+1):
    if ans%i==0:
        cnt+=1
print(cnt)

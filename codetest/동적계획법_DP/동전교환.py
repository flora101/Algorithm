import sys
input = sys.stdin.readline
n = int(input())
money = list(map(int,input().split()))
m = int(input())
dp = [2147000000]*(m+1)
for i in money:
    for j in range(i,m+1):
        if i == j:
            dp[j]=1
        dp[j]=min(dp[j], dp[j-i]+1)
# print(dp)
print(dp[m])

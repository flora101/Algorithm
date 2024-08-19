n,m=map(int,input().split())
score,time = [], []
for i in range(n):
    a,b = map(int,input().split())
    score.append(a)
    time.append(b)
dp = [0]*(m+1)
for i in range(n):
    for j in range(m,time[i]-1,-1):
        dp[j] = max(dp[j],dp[j-time[i]]+score[i])
print(max(dp))

count,weight= map(int,input().split())
dp = [0]*(weight+1)
w,v = [],[]
for i in range(count):
    a,b = map(int,input().split())
    w.append(a)
    v.append(b)
for i in range(count):
    for j in range(w[i],weight+1):
        dp[j]= max(dp[j],dp[j-w[i]]+v[i])
print(max(dp))

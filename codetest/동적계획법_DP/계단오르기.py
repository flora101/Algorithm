import sys
input = sys.stdin.readline
n=int(input())
dp=[0]*(n+1)
def DFS(a):
    # print(dp)
    if a<3:
        dp[a]=a
        return a
    else:
        dp[a]=DFS(a-1)+DFS(a-2)
        return dp[a]
print(DFS(n))

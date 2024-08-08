import sys
input = sys.stdin.readline
n=int(input())
dp = [0]*(n+1)
def DFS(a):
    if a <3:
        dp[a]=a
        return a
    else:
        return DFS(a-1)+DFS(a-2)
print(DFS(n+1))
